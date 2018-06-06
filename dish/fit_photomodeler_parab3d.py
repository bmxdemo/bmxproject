from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
from scipy.optimize import minimize as fmin
from scipy.optimize import curve_fit
ion()

# Usage:
# ipython
# import fit_photomodeler_parab3d as fpp
# x,y,z=fpp.getdata('data/16Oct2017_dish_surface.txt')
# pfit=fpp.fitparab(x,y,z)

def getdata(fname):
    # Get data
    if fname=='mockdata':
        # Generate mock data
        # "real" parameters
        p=array([.7, 1, .1, .2, -3, 30, 5, 0])

        # Generate (x,y) grid
        x=linspace(-1,1,10);
        y=linspace(-1,1,10);
        x,y=meshgrid(x,y)

        # 2d arrays to 1d arrays
        x=x.ravel()
        y=y.ravel()

        # define parabola
        z=zmod((x,y),*p) 

    else:
        # Get real data from PhotoModeler in meters
        dat=loadtxt(fname)
        # First column is the point ID.
        # Convert to mm
        x=dat[:,1]*1000 
        y=dat[:,2]*1000
        z=dat[:,3]*1000

    return x,y,z

def rotmat(x,y,z):
    # Input rotation angles x, y, z should be in degrees, so convert to radians
    x=x*pi/180
    y=y*pi/180 
    z=z*pi/180

    Rx = array([[1,0,0] , [0, cos(x), -sin(x)], [0, sin(x), cos(x)]])
    Ry = array([[cos(y), 0, sin(y)], [0,1,0], [-sin(y), 0, cos(y)]])
    Rz = array([[cos(z), -sin(z), 0], [sin(z), cos(z), 0], [0,0,1]])

    return mat(Rz)*mat(Ry)*mat(Rx)


def applyrot(R,x,y,z,x0=0,y0=0,z0=0):
    xr=zeros(x.shape)
    yr=zeros(y.shape)
    zr=zeros(z.shape)

    for k,val in enumerate(x):
        p0=mat([x[k]-x0,y[k]-y0,z[k]-z0])
        pr=R*p0.T # do rotation
        xr[k]=pr[0]+x0
        yr[k]=pr[1]+y0
        zr[k]=pr[2]+z0

    return xr,yr,zr

def zaxeq(ax,x,y,z):
    # Create cubic bounding box to simulate equal aspect ratio
    max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max()
    xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x.max()+x.min())
    yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y.max()+y.min())
    zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(z.max()+z.min())
    # Comment or uncomment following both lines to test the fake bounding box:
    for xb, yb, zb in zip(xb, yb, zb):
        ax.plot([xb], [yb], [zb], 'w')


def zmod(data,*p):
    """Params are:
    p[0], p[1] -        coefficients on x^2 and y^2 (currently p[1]=0 always)
    p[2], p[3], p[4] -  x,y,z translations
    p[5], p[6], p[7] -  x,y,z rotations in degrees
    """
    sz=data[0].shape

    x=ravel(data[0])
    y=ravel(data[1])
    # Fit for curvature
    z=p[4] + p[0]*(x-p[2])**2 + p[0]*(y-p[3])**2

    #Fit for rotation:
    #R=rotmat(p[5],p[6],p[7]) 

    #Don't fit for rotation:
    R=rotmat(0,0,0) 

    dum,dum,zrot=applyrot(R,x,y,z,p[2],p[3],p[4])
    zrot=reshape(zrot,sz)

    return zrot

#def zmod(data,*p):
#    """Params are:
#    p[0], p[1] -        coefficients on x^2 and y^2 (currently p[1]=0 always)
#    p[2], p[3], p[4] -  x,y,z translations
#    p[5], p[6], p[7] -  x,y,z rotations in degrees
#    """
#    sz=data[0].shape
#
#    x=ravel(data[0])
#    y=ravel(data[1])
#    # Fit for curvature
#    z=p[0]*x**2 + p[0]*y**2
#
#    #Fit for rotation:
#    R=rotmat(p[5],p[6],p[7])
#
#    #Don't fit for rotation:
#    R=rotmat(0,0,0) 
#
#    xrot,yrot,dum=applyrot(R,x,y,z,p[2],p[3],p[4])
#    xrot=reshape(xrot,sz)
#    yrot=reshape(yrot,sz)
#
#    #Fit for translation
#    zrottrans=p[4] + p[0]*(xrot-p[2])**2 + p[0]*(yrot-p[3])**2
#    zrottrans=reshape(zrottrans,sz)
#
#    return zrottrans

def plot3d(x,y,z,*args):    
    gcf()
    ax=gca()
    if not hasattr(ax,'get_zlim'):
        ax=gcf().add_subplot(111,projection='3d')
    ax.plot(x,y,z,*args)


def fitparab(x,y,z,doplot=True,pguess=None):
    """Fit x,y,z photogrammetry data to a 3d parabola"""

    #########################
    # Fit data
    if pguess is None:
        pguess = array([8.6e-5, 0, 0, 0, 0, 0, 0, 0])
        low = array([0,   0,   -inf, -inf, -inf, -30, -30, -30])
        hi  = array([inf, inf,  inf,  inf,  inf,  30,  30,  30])

    pfit=curve_fit(zmod,(x,y),z,p0=pguess,method='trf',bounds=(low,hi))[0]
    #pfit=curve_fit(zmod,(x,y),z,p0=pguess,method='lm')[0]
    print pfit
    zfit=zmod((x,y),*pfit)
    #print ','.join(map(str, zfit))
    resids=z-zfit
    #print resids

    if doplot:

        ######################
        # Data
        fig=figure(1)
        clf()


        ax=fig.add_subplot(111,projection='3d')
        h1,=ax.plot(x,y,z,'.k',label='data')
        ax.set_aspect('equal',adjustable='box')

        xx=linspace(min(x),max(x),100)
        yy=linspace(min(y),max(y),100)
        xx,yy=meshgrid(xx,yy)
        zz=zmod((xx,yy),*pfit)
        h2=ax.plot_surface(xx,yy,zz)

        zaxeq(ax,xx,yy,zz)

        xlabel('x (mm)')
        ylabel('y (mm)')
        ax.set_zlabel('z (mm)')
        h2=Rectangle((0,0),1,1,fc='b',alpha=1)
        legend([h1,h2],['data','best fit parabola'])

        ###############
        # Resids
        fig=figure(2)
        clf()

        ax=fig.add_subplot(111,projection='3d')
        ax.plot(x,y,resids,'.k',label='residuals')
        ax.plot_trisurf(x,y,zeros(z.shape),color='b',alpha=.2,linewidth=0)
        xlabel('x (mm)')
        ylabel('y (mm)')
        ax.set_zlabel('z-zfit (mm)')
        legend()
    
    return pfit


