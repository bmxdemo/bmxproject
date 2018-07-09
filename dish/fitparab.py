from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import curve_fit

def getdata(fname):
    """Load in photomodeler data. Sort by target ID. Data assumed to be in
    meters, converts to mm. Outputs x, y, and z."""

    # Get data
    dat=loadtxt(fname)

    #Sort data
    ind=argsort(dat[:,0])

    # Convert to mm
    x=dat[ind,1]*1000 
    y=dat[ind,2]*1000
    z=dat[ind,3]*1000

    return x,y,z


class fitparab(object):
    
    def __init__(self, x=None, y=None, z=None, pguess=None, fitrot=[False, False, False]):
        """Fit a 2D parabola to x,y,z points.
        - pguess are initial guess for fit params (see zmod)
        - fitrot is a three element array of True/False, one for x, y, and z
          respectively, where if False, the fit for a rotation around that axis is
          not done.  (Default all False.)
        """

        self.x = x
        self.y = y
        self.z = z

        if pguess is None:
            #Initial Parameters
            self.pguess=[8.6e-5, 0, 2330, -870, 8, 0.5, 0, 0]
        
        self.fitrot = fitrot

        if x is not None:
            self.fit()


    def fit(self): 
        """Do the non-linear least squares fit of a parabola to the data.
        x, y and z are the data points, pguess is the initial parameter gress
        vector (see zmod for definition). fitrot is a three element vector of
        True/False values, where if False, the rotation about that axis is not
        fit. (Default all False)"""


        #Fitting Data
        self.pfit = curve_fit(self.zmod,(self.x,self.y,self.fitrot), self.z,
                       p0=self.pguess, method='lm')[0]
        self.zfit = self.zmod((self.x,self.y,self.fitrot),*self.pfit)


    def rotmat(self, x, y, z, fitrot=[True,True,True]):
        """Return a rotation matrix that rotates about fixed x, y, z axes. 
        Input rotation angles x, y, z should be in degrees. fitrot three element
        vector for x, y, and z axes, respectively, where if element if False,
        the corresponding rotation is not done. This is needed for non-linear 
        fitters. (Default True). By default [True,True,True]"""
        
        # Convert to radians
        x=x*pi/180
        y=y*pi/180
        z=z*pi/180

        if not fitrot[0]:
            x = 0
            
        if not fitrot[1]:
            y = 0

        if not fitrot[2]:
            z = 0


        # Get rotation matrices
        Rx = array([[1,0,0],[0,1-2*(sin(x/2)**2),-2*cos(x/2)*sin(x/2)],[0,2*cos(x/2)*sin(x/2),1-2*(sin(x/2)**2)]])
        Ry = array([[1-2*(sin(y/2)**2),0,2*cos(y/2)*sin(y/2)],[0,1,0],[-2*cos(y/2)*sin(y/2),0,1-2*(sin(y/2)**2)]])
        Rz = array([[1-2*(sin(z/2)**2),-2*cos(z/2)*sin(z/2),0],[2*cos(z/2)*sin(z/2),1-2*(sin(z/2)**2),0],[0,0,1]]) 

        # Return dot product of rotation matrices

        return dot(dot(Rx,Ry),Rz)


    def applyrot(self, R, x, y, z, x0=0, y0=0, z0=0):
        """Rotate a set of x,y,z points by the given rotation matrix. Rotation
        is done about the origin defined by x0, y0, z0, default (0,0,0)."""

        # Turn scalars to vectors
        x = np.atleast_1d(x)
        y = np.atleast_1d(y)
        z = np.atleast_1d(z)
        xr=zeros(x.shape)
        yr=zeros(y.shape)
        zr=zeros(z.shape)

        for k,val in enumerate(y):
            p0=mat([x[k]-x0,y[k]-y0,z[k]-z0])
            pr=R*p0.T # do rotation
            xr[k]=pr[0]+x0
            yr[k]=pr[1]+y0
            zr[k]=pr[2]+z0

        return xr,yr,zr

    def zmod(self, data, *p):
        """2D parabola. Params are:
        p[0], p[1] -        coefficients on x^2 and y^2 (currently p[1]=0 always!!!)
        p[2], p[3], p[4] -  x,y,z translations
        p[5], p[6], p[7] -  x,z rotations in degrees
        """

        sz=data[0].shape

        x=ravel(data[0])
        y=ravel(data[1])
        fitrot=data[2]

        # Fit for curvature
        z=p[4] + p[0]*(x-p[2])**2 + p[0]*(y-p[3])**2

        #Fit for rotation:
        R=self.rotmat(p[5],p[6],p[7],fitrot)

        dum,dum,zrot=self.applyrot(R,x,y,z,p[2],p[3],p[4])
        zrot=reshape(zrot,sz)

        return zrot





