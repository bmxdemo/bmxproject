import numpy as np
import matplotlib.pyplot as plt
plt.ion()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.coordinates import get_sun
from astropy import constants as const
import scipy.optimize as opt
import math as m
import time

'''
READ ME
-------
There are three classes: Fit, BMXSim, and Dish. 
Use by initializing a Fit object.

import fringefit as ff
f = ff.Fit()

Here you may specify the tag, the frequency and time window, and whether you would like to fit to data or a simulation.
If the data is not specified, it is assumed that you will generate a simulation.
A simulation and four dishes (NESW) are initialized as: f.sim, f.sim.dn, f.sim.de, f.sim.ds, f.sim.dw
Set simulation parameters and run: f.gensim(dish0,dish1) (OR skip this step if fitting to data)

Then run the fit: params = f.dofit()
'''

class Fit():

    def __init__(self, tag='190301', data=None, label=None, fstart=1.1e9, fstop=1.5e9, tstart=None, tstop=None):
        self.label = label
        self.sim = BMXSim(tag[0:6])
        self.sim.fstart = fstart
        self.sim.fstop = fstop
        if tstart is not None and tstop is not None: 
            self.sim.tstart = tstart
            self.sim.tstop = tstop
        elif len(tag)>6: 
            if tstart is None: self.sim.tstart = int(tag[7:9])
            if tstop is None: self.sim.tstop = int(tag[7:9])+1
        if data is None: # if data is not specified then generate simulated data to fit
            self.usesim = True
            print('Use self.sim to specify simulation parameters.\nThen run self.gensim(dish0,dish1).')
        else:
            self.usesim = False
            self.sim.nfreq = data.shape[1]
            self.sim.ntimes = data.shape[0]
            self.sim.getframe()
            self.sim.getcyga()
            self.sim.getfreq()
            self.R_data = data

    def dofit(self):
        # completes fit to R_data and returns parameters found
        print('initial fit...')
        t = time.time()
        fit_init = self.fit_all()
        print('find time delay...')
        tau0 = self.fit_tau(fit_init.x[1:])
        print('final fit...')
        fit_fin = self.fit_all(tau0)
        print('...took {:0.1f} sec'.format(time.time()-t))
        return fit_fin

    def gensim(self, dish0, dish1):
        # generates a new simulation with parameters set in self.sim
        self.sim.getframe()
        self.sim.getcyga()
        self.sim.getfreq()
        # update dish position and pointing
        dish0.update_pos() # East
        dish0.update_p()
        dish0.update_sigma()
        dish1.update_pos() # West
        dish1.update_p()
        dish1.update_sigma()
        # generate signal
        self.sim.simwf(dish0, dish1)
        self.sim.addnoise()
        self.R_data = self.sim.R_noise[0]

    def func(self, tau, a , p0_pol, sigma, bx, by=0):
        tau = tau*1e-9*u.s # time delay, scale tau ns => O(1)
        p_pol = np.array((m.radians(p0_pol), 0)) # pointing errors, deg->radian
        p_az = np.array((m.radians(90), 0))
        sigma = m.radians(sigma) # beam width, deg->radian
        b = np.array((bx,by,0))*u.m # vector between dishes
        # solve for p and v
        p = np.zeros((2,3)) # pointing error unit vectors, two dishes
        v = np.zeros((2, self.sim.ntimes)) # guassian envelope as source passes overhead
        for dish in range(2):
            p[dish] = np.array((np.sin(p_pol[dish])*np.sin(p_az[dish]),np.sin(p_pol[dish])*np.cos(p_az[dish]),np.cos(p_pol[dish])))
            for t in range(self.sim.ntimes):
                v[dish,t] = a*np.exp(-np.dot(self.sim.cyga_s[:,t]-p[dish],self.sim.cyga_s[:,t]-p[dish])/(2*sigma**2))
        # solve for R
        bdots = np.dot(b, self.sim.cyga_s)
        deltaomega = 2*np.pi*self.sim.deltaf
        R = np.zeros((self.sim.ntimes,self.sim.nfreq),dtype=complex)
        for ifreq in range(self.sim.nfreq):
            omega = 2*np.pi*self.sim.freq[ifreq]
            R[:,ifreq] = v[0]*v[1]*np.exp(1j*omega*(tau + bdots/const.c))*np.sinc(deltaomega/2*(tau + bdots/const.c))
        return np.array((R.real,R.imag))

    def residual(self, p):
        # residual error for use in scipy.optimize.least_squares
        res = self.R_data - self.func(*p)[0]
        return res.reshape(self.sim.nfreq*self.sim.ntimes)

    def fit_all(self,tau_init=1):
        # least squares fit to all parameters, can specify initial tau guess
        # parameter array: (tau, a, p0_pol, p0_az, sigma, bx) -> see func()
        p0 = np.array((tau_init,1,0,2.5,10)) # initial guess
        bounds = np.array(((1e-3,0,-90,0,0),(1e3,2,90,10,20)))
        fit = opt.least_squares(self.residual, p0, bounds=bounds)
        return fit

    def sumsqrerr(self,p):
        # sum of squared errors for parameters p
        res = self.R_data - self.func(*p)[0]
        res = res.reshape(self.sim.nfreq*self.sim.ntimes)
        return sum(res**2)

    def brute_tau(self,p0,tmin,tmax,tn):
        # finds tau with minimum sum squared error over specified range and number of points
        # specify p0 as initial fit result for other parameters
        if (tmax-tmin)/tmin > 10:
            tau = np.geomspace(tmin,tmax,tn) # logarthimic point spacing
        else:
            tau = np.linspace(tmin,tmax,tn) # linear point spacing
        for i,t in enumerate(tau):
            p = [t,*p0]
            err = self.sumsqrerr(p)
            if i is 0:
                minerr = err
                besttau = t
            else:
                if minerr > err:
                    minerr = err
                    besttau = t
        return besttau

    def fit_tau(self,x0):
        # find tau by brute force with narrowing search parameters
        tau1 = self.brute_tau(x0,1e-3,1e3,100) # wide search
        strtau = '%.2e'%(tau1)
        exp = int(strtau[5:])
        tau2 = self.brute_tau(x0,1*10**exp,1*10**(exp+1),500) # fine search
        return tau2

    def reducedata(self, factor, opt=None):
        # speeds up fitting by set factor by reducing simulated data by that amount
        # set opt to 'time' to reduce only in time or 'freq' to reduce only in freq
        # run gensim() afterwards to regenerate simulation
        if opt is 'time':
            self.sim.ntimes = int(self.sim.ntimes/factor)
        elif opt is 'freq':
            self.sim.nfreq = int(self.sim.nfreq/factor)
        else:
            self.sim.ntimes = int(self.sim.ntimes/factor)
            self.sim.nfreq = int(self.sim.nfreq/factor)
    
    def pererror(self, real, fit):
        # percent error of fit vs simulated parameters
        perr = np.zeros(len(real)+1)
        for i in range(len(real)):
            perr[i] = abs((real[i]-fit[i])/real[i])*100
        perr[len(real)] = np.mean(perr[0:len(real)])
        return perr
        
    def plotfit(self, fitparams, dish0=None, dish1=None):
        Rfit = self.func(*fitparams)
        plt.figure(figsize=(12,10))
        # Data
        ax1=plt.subplot(311)
        plt.imshow(self.R_data,cmap='jet',extent=(self.sim.fstart,self.sim.fstop,self.sim.tstop,self.sim.tstart),aspect='auto')
        plt.colorbar(pad=0)
        plt.clim(-1,1)
        plt.xticks([])
        plt.ylabel('\\textbf{UTC Time [Hr]}')
        if self.usesim is True: plt.title('\\textbf{Simulated Data + Noise}', loc='left')
        else: plt.title('\\textbf{Mean Filtered Data}', loc='left', fontsize='22')
        # Fit
        ax2=plt.subplot(312)
        plt.imshow((Rfit[0]),cmap='jet',extent=(self.sim.fstart,self.sim.fstop,self.sim.tstop,self.sim.tstart),aspect='auto')
        plt.colorbar(pad=0)
        plt.clim(-1,1)
        plt.xticks([])
        plt.ylabel('\\textbf{UTC Time [Hr]}')
        plt.title('\\textbf{Fit Result}', loc='left', fontsize='22')
        # Residuals
        ax2=plt.subplot(313)
        plt.imshow((self.R_data - Rfit[0]),cmap='jet',extent=(self.sim.fstart,self.sim.fstop,self.sim.tstop,self.sim.tstart),aspect='auto')
        plt.colorbar(pad=0)
        plt.clim(-1,1)
        plt.xlabel('\\textbf{Frequency [Hz]}')
        plt.ylabel('\\textbf{UTC Time [Hr]}')
        plt.title('\\textbf{Residual}', loc='left', fontsize='22')
        # Formatting
        plt.suptitle('\\textbf{Cygnus A Signal, %s, %s}'%(self.sim.tag, self.label))
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, right=0.8, hspace=0.2)
        # Simulation Parameter table
        if self.usesim is True:   
            plt.text(1.3,2.1,
                        '\\textbf{Sim Params}\n'
                        '$A$ = 1.00\n'
                        '$b_x$ = %.2f m\n'
                        '$b_y$ = %.2f m\n'
                        '$\\tau$ = %.1e s\n'
                        '$\sigma$ = %.1f deg\n'
                        '$p_{0\\theta}$ = %.1f deg\n'
                        '$p_{0\\phi}$ = %.1f deg\n'
                        '$p_{1\\theta}$ = %.1f deg\n'
                        '$p_{1\\phi}$ = %.1f deg'
                        %((dish0.x-dish1.x)/u.m,
                         (dish0.y-dish1.y)/u.m,
                         (dish0.tau-dish1.tau)/u.s,
                         dish0.sigma_d/u.deg,
                         dish0.p_pol/u.deg,
                         dish0.p_az/u.deg,
                         dish1.p_pol/u.deg,
                         dish1.p_az/u.deg),
                    transform=ax2.transAxes,
                    ha='center',
                    va='center',
                    bbox=dict(boxstyle='round',facecolor='none'))
        # Fit Parameter table
        plt.text(1.32,1,
                    '\\textbf{Fit Params}\n'
                    '$A$ = %.2f\n'
                    '$b_x$ = %.2f m\n'
                    '$b_y$ = %.2f m\n'
                    '$\\tau$ = %.1e s\n'
                    '$\sigma$ = %.1f deg\n'
                    '$p_{0\\theta}$ = %.1f deg\n'
                    '$p_{0\\phi}$ = %.1f deg\n'
                    '$p_{1\\theta}$ = %.1f deg\n'
                    '$p_{1\\phi}$ = %.1f deg'
                    %(fitparams[1],
                    fitparams[4], #b_x
                    fitparams[5], #b_y
                    fitparams[0]*1e-9, #tau
                    fitparams[3], #sigma
                    fitparams[2], #po_pol
                    90, #p0_az, p0 kept in E-W plane
                    0, #p1_pol, p1 kept at zero
                    0), #p1_az
                transform=ax2.transAxes,
                ha='center',
                va='center',
                bbox=dict(boxstyle='round',facecolor='none'))
        plt.savefig('plots/fit_test.png')
        
    
        
class BMXSim():

    def __init__(self, tag=None):
        # data window
	    # define either by step or by number
        #self.tstep = 128.*33/1000/60/60 # 33ms * 128 average in hours
        self.ntimes = 640 
        self.tstart = 14.0
        self.tstop = 14.75
	    #self.fstep = (1.5e9-1.1e9)/2048 # 2048 freq bins, bmx range
        self.nfreq = 1024
        self.fstart = 1.3e9
        self.fstop = 1.5e9
        # get tag info
        if tag is None: self.tag = '190301'
        else: self.tag = tag
        self.parsetag()
        # define telescope location
        self.location = EarthLocation(lat = 40.869951*u.deg, lon = -72.866072*u.deg, height = 20*u.m)
        # get telescope frame
        self.getframe()	
        # get cygnus a
        self.getcyga()
        # get freq range
        self.getfreq()
        # define dishes
        self.de = Dish(x=5.,label='E')  
        self.dw = Dish(x=-5.,label='W')
        self.dn = Dish(y=5.,label='N')
        self.ds = Dish(y=-5.,label='S')

    def parsetag(self):
        year = self.tag[0:2]
        month = self.tag[2:4]
        day = self.tag[4:6]
        self.time_str = '20%s-%s-%s 00:00:00' %(year,month,day)

    def getframe(self):
        utcoffset = -5 # EST
        midnight = Time(self.time_str) - utcoffset*u.hour
        # get time by range and N
        delta_midnight = np.linspace(self.tstart+utcoffset, self.tstop+utcoffset, self.ntimes)*u.hour
        # OR get time by range and step size
        #delta_midnight = np.arange(self.tstart+utcoffset, self.tstop+utcoffset, self.tstep)*u.hour
	    #self.ntimes = delta_midnight.size 
        self.times = midnight + delta_midnight
        self.frame = AltAz(obstime = self.times, location = self.location)

    def getcyga(self):
        self.cyga = SkyCoord.from_name('Cygnus A')
        self.cyga_altaz = self.cyga.transform_to(self.frame)
        alpha = 90.*u.deg - self.cyga_altaz.alt # define alpha -> angle from zenith
        self.cyga_alpha = alpha * (np.pi*u.rad)/(180*u.deg) # convert to radians
        # define unit vector s pointing to cygnus a
        s_x = np.sin(alpha)*np.sin(self.cyga_altaz.az) # +x-axis = east
        s_y = np.sin(alpha)*np.cos(self.cyga_altaz.az) # +y-axis = north
        s_z = np.cos(alpha)
        self.cyga_s = np.array((s_x, s_y, s_z))
        self.cyga_z = 0.056075 # redshift from wiki
        self.cyga_f = const.c/((1+self.cyga_z)*0.21*u.m) # observed frequency, 0.21 = 21cm emitted wavelength
        
    def getfreq(self):
    	# define frequencies to sweep
        # by range and N
        self.freq = np.linspace(self.fstart, self.fstop, self.nfreq)/u.s
        # OR by range and step size
    	#self.freq = np.arange(self.fstart, self.fstop, self.fstep)/u.s
        #self.nfreq = self.freq.size
        self.deltaf = self.freq[1]-self.freq[0]

    def correlate(self, dish0, dish1, freq, deltaf=None, b=None, v0=None, v1=None):
        # Gets correlated signal for a single frequency
        if b is None: b = dish0.pos - dish1.pos # vector between dish positions
        if v0 is None: v0 = dish0.signal(self.cyga_s) # gaussian envelope from dish 0
        if v1 is None: v1 = dish1.signal(self.cyga_s) # gaussian envelope from dish 1
        tau = dish0.tau - dish1.tau
        omega = 2*np.pi*freq
        bdots = np.dot(b,self.cyga_s)
        if deltaf is None: # single frequency case
            R = v0*v1*np.exp(1j*omega*(tau + bdots/const.c))
        else: # average over frequency bin freq +/- deltaf/2
            deltaomega = 2*np.pi*deltaf
            R = v0*v1*np.exp(1j*omega*(tau + bdots/const.c))*np.sinc(deltaomega/2*(tau + bdots/const.c))
        return R

    def simwf(self, dish0, dish1):
        # simulate waterfall plot
        b = dish0.pos - dish1.pos #vector between dish positions
        self.bmag = np.linalg.norm(b)*u.m
        v0 = dish0.signal(self.cyga_s) # gaussian envelope from dish 0
        v1 = dish1.signal(self.cyga_s) # gaussian envelope from dish 1
        # calculate response signals
        R = np.zeros((self.ntimes,self.nfreq),dtype=complex)
        for i,f in enumerate(self.freq): # get R for all frequencies
            R[:,i] = self.correlate(dish0, dish1, f, self.deltaf, b, v0, v1)
        self.R = np.array((R.real,R.imag)) # save real and imaginary R

    def plotwf(self,dish0,dish1,R = None):
        # plot simulated waterfall plot
        if R is None: R = self.R
        fig=plt.figure(figsize=(10,5))
        # Real part
        ax1=plt.subplot(211)
        plt.imshow(R[0].T,cmap='jet',extent=(self.fstart,self.fstop,self.tstop,self.tstart),aspect='auto')
        plt.colorbar(pad=0)
        plt.clim(-1,1)
        #plt.xscale('log')
        plt.xticks([])
        plt.ylabel('UTC Time [Hr]')
        plt.title('Real', loc='left')
        # Imaginary part
        ax2=plt.subplot(212)
        plt.imshow(R[1].T,cmap='jet',extent=(self.fstart,self.fstop,self.tstop,self.tstart),aspect='auto')
        plt.colorbar(pad=0)
        plt.clim(-1,1)
        #plt.xscale('log')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('UTC Time [Hr]')
        plt.title('Imaginary', loc='left')
        # Formatting
        plt.suptitle('Cygnus A Simulated Signal, %s'%(self.tag))
        plt.tight_layout()
        plt.subplots_adjust(top=0.92, right=0.9,hspace=0.15)
        # Parameter table
        plt.text(1.1955555,1.1,
                    '%s $\\times$ %s\n'
                    '$b_%s$ = (%.1f, %.1f) m\n'
                    '$b_%s$ = (%.1f, %.1f) m\n'
                    '$\\tau$ = %.1e s\n'
                    '$\sigma$ = %s\n'
                    '$p_%s$ = (%s, %s) deg\n'
                    '$p_%s$ = (%s, %s) deg'
                    %(dish0.label,dish1.label,
                    dish0.label,dish0.x,dish0.y,
                    dish1.label,dish1.x,dish1.y,
                    (dish0.tau-dish1.tau)/u.s,
                    str(dish0.sigma_d),
                    dish0.label,str(dish0.p_pol/u.deg),str(dish0.p_az/u.deg),
                    dish1.label,str(dish1.p_pol/u.deg),str(dish1.p_az/u.deg)),        
                transform=ax2.transAxes,
                fontsize=12,
                ha='center',
                va='center',
                bbox=dict(boxstyle='round',facecolor='none'))

    def addnoise(self):
        # adds random noise to R simulation
        Rn_real = self.R[0] + np.random.normal(0,0.05,(self.nfreq,self.ntimes))
        Rn_imag = self.R[1] + np.random.normal(0,0.05,(self.nfreq,self.ntimes))
        self.R_noise = np.array((Rn_real,Rn_imag))




class Dish():
    def __init__(self, x=0., y=0., z=0.,label=''):
        # position coordinates in meters (from bmx center/tower)
        self.x = x
        self.y = y
        self.z = z
        self.pos = np.array((self.x, self.y, self.z))*u.m
        # label
        self.label = label
        # pointing error
        self.p_pol = 0.*u.deg # polar angle from zenith
        self.p_az = 0.*u.deg # azimuthal angle from north (+y)
        self.p = np.array((np.sin(self.p_pol)*np.sin(self.p_az),
                           np.sin(self.p_pol)*np.cos(self.p_az),
                           np.cos(self.p_pol))) # unit vector p
        # beam width, circular dish
        self.sigma_d = 2.5*u.deg
        self.sigma = self.sigma_d * (np.pi)/(180*u.deg) # convert to radians
        # signal time delay (cable len, digitizer, etc.)
        self.tau = 0.*u.s

    def update_pos(self):
        self.pos = np.array((self.x, self.y, self.z))*u.m

    def update_p(self):
        self.p = np.array((np.sin(self.p_pol)*np.sin(self.p_az),
                           np.sin(self.p_pol)*np.cos(self.p_az),
                           np.cos(self.p_pol)))
                           
    def update_sigma(self):
        self.sigma = self.sigma_d * (np.pi)/(180*u.deg) # convert to radians

    def signal(self, cyga_s):
        # returns gaussian signal from source at angle alpha from zenith
        V0 = 1. # norm amplitude
        sig = np.zeros(cyga_s.shape[1])
        for i in range(cyga_s.shape[1]):
            sig[i] = V0*np.exp(-np.dot(cyga_s[:,i]-self.p,cyga_s[:,i]-self.p) / (2*self.sigma**2))
        return sig





