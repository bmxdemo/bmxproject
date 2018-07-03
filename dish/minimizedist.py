from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import minimize as fmin
import fitparab

# Instantiate fitparab with no data to use its functions
fp = fitparab.fitparab()

class minimizedist(object):

    def __init__(self, x1, y1, z1, x2, y2, z2):
        """Initialize distance minimization. Fits one set of photomodeler points
        to a second set. Fit parameters are 3 of translation, 3 of scaling, and
        three of rotation"""

        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

        self.distminimize()
        self.plotresids()

        return

    def mod(self, p,*data):
        #p[0] p[1] p[2] - x,y,z scaling
        #p[3] p[4] p[5] - x,y,z translations
        #p[6] p[7] p[8] - x,y,z rotations

        x2 = data[0] 
        y2 = data[1]
        z2 = data[2]
        x1 = data[3]
        y1 = data[4]
        z1 = data[5]

        xmod=p[0]*(x2-p[3])
        ymod=p[1]*(y2-p[4])
        zmod=p[2]*(z2-p[5])
        R=fp.rotmat(p[6],p[7],p[8])
        xrot,yrot,zrot=fp.applyrot(R,xmod,ymod,zmod,p[3],p[4],p[5])

        #Distance Formula
        dist=sqrt((x1-xrot)**2 + (y1-yrot)**2 + (z1-zrot)**2)

        #Summation of Distances
        distsum=sum(dist)

        return distsum


    def distminimize(self):
        """Do the minimization"""
        #Minimization
        self.distmin = fmin(self.mod, [0,0,0,0,0,0,0,0,0], args=(self.x2,self.y2,self.z2,self.x1,self.y1,self.z1))
        
    def plotresids(self, units='mm'):
        """Make plots"""

        distmin = self.distmin

        #Modify Using Optimized Parameters
        xopt=(distmin.x[0])*(self.x2-distmin.x[3])
        yopt=(distmin.x[1])*(self.y2-distmin.x[4])
        zopt=(distmin.x[2])*(self.z2-distmin.x[5])
        R=fp.rotmat(distmin.x[6],distmin.x[7],distmin.x[8])
        xrot,yrot,zrot=fp.applyrot(R,xopt,yopt,zopt,distmin.x[3],distmin.x[4],distmin.x[5])

        #Plot Residuals
        figure(1)
        clf()

        xr = self.x1 - self.x2
        yr = self.y1 - self.y2
        zr = self.z1 - self.z2
        
        xrr = self.x1 - xrot
        yrr = self.y1 - yrot
        zrr = self.z1 - zrot

        subplot(1,2,1)
        plot(xr, '.', label='X')
        plot(yr, '+', label='Y')
        plot(zr, 'o', label='Z')
        legend(loc='best')
        title('Raw Residuals')
        xlabel('data point index')
        ylabel('residuals ({:s})'.format(units))

        subplot(1,2,2)
        plot(xrr, '.', label='X')
        plot(yrr, '+', label='Y')
        plot(zrr, 'o', label='Z')
        legend(loc='best')
        title('Optimized Residuals')
        xlabel('data point index')
        ylabel('residuals ({:s})'.format(units))
        


        #Plot Histograms
        figure(2)
        clf()

        subplot(1,2,1)
        hist(xr, bins=10, label='X (std={:0.2f})'.format(std(xr)))
        hist(yr, bins=10, label='Y (std={:0.2f})'.format(std(yr)))
        hist(zr, bins=10, label='Z (std={:0.2f})'.format(std(zr)))
        legend(loc='best')
        title('Raw')
        xlabel('residuals ({:s})'.format(units))
        ylabel('counts')

        subplot(1,2,2)
        hist(self.x1-xrot, bins=10, label='X (std={:0.2f})'.format(std(xrr)))
        hist(self.y1-yrot, bins=10, label='Y (std={:0.2f})'.format(std(yrr)))
        hist(self.z1-zrot, bins=10, label='Z (std={:0.2f})'.format(std(zrr)))
        legend(loc='best')
        title('Optimized')
        xlabel('residuals ({:s})'.format(units))
        ylabel('counts')

        show()
