from numpy import *
import matplotlib
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

print matplotlib.__version__

def rotmat(x,y,z):
    # Input rotation angles x, y, z should be in degrees, so convert to radians
    x=x*pi/180
    y=y*pi/180
    z=z*pi/180

    Rx=array([[1,0,0], [0, cos(x), sin(x)], [0, -sin(x), cos(x)]])
    Ry=array([[cos(y), 0, -sin(y)], [0,1,0], [sin(y), 0, cos(y)]])
    Rz=array([[cos(z), sin(z), 0], [-sin(z), cos(z), 0], [0,0,1]])

    return mat(Rx)*mat(Ry)*mat(Rz)

# Get the dish surface xyz points from PhotoScan
da_full=np.loadtxt('BMX_Petal_xyz.txt')
# Reduce the number of points by a factor of 1000
da=da_full[::1000]
x=da[:,0]
y=da[:,1]
z=da[:,2]    

# Define rotation matrix
R=rotmat(0,0,0)
xr=[]
yr=[]
zr=[]
for k,val in enumerate(x):
    p0=mat([x[k],y[k],z[k]]) # point initially
    pr=R*p0.T # do rotation on point
    xr.append(pr[0])
    yr.append(pr[1])
    zr.append(pr[2])
xr=array(xr)
yr=array(yr)
zr=array(zr)

# Plot
fig=figure()
clf()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,color='b')
ax.scatter(xr,yr,zr,color='r')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
show()
