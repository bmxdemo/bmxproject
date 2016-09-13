from numpy import *
from matplotlib.pyplot import *

def rotmat(x,y,z):
    # Input rotation angles x, y, z should be in degrees, so convert to radians
    x=x*pi/180
    y=y*pi/180
    z=z*pi/180

    Rx = array([[1,0,0] , [0, cos(x), sin(x)], [0, -sin(x), cos(x)]])

    # Right now don't rotate around y or z axes
    Ry=1
    Rz=1

    return mat(Rx)*identity(Rx.shape[0])*identity(Rx.shape[0])

    
    
x=linspace(-1,1,30);
y=linspace(-1,1,30);
x,y=meshgrid(x,y)

# 2d arrays to 1d arrays for scatter
x=x.ravel()
y=y.ravel()

# define parabola
z=x**2+y**2

# Define rotation matrix
R=rotmat(45,0,0)
xr=[]
yr=[]
zr=[]
for k,val in enumerate(x):
    p0=mat([x[k],y[k],z[k]])
    pr=R*p0.T # do rotation
    xr.append(pr[0])
    yr.append(pr[1])
    zr.append(pr[2])
xr=array(xr)
yr=array(yr)
zr=array(zr)

# plot
fig=figure()
clf()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,color='b')
ax.scatter(xr,yr,zr,color='r')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')

