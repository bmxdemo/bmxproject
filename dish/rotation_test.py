import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Demonstration of the ability of 
# fit_photomodeler_parab3d.py to rotate a data
# set by specified angles x, y, and z using
# the x, y, and z rotation matrices.

def rotmat(x,y,z):
    # Input rotation angles x, y, z should be in degrees, so convert to radians
    x=x*np.pi/180
    y=y*np.pi/180 
    z=z*np.pi/180

    Rx = np.array([[1,0,0] , [0, np.cos(x), -np.sin(x)], [0, np.sin(x), np.cos(x)]])
    Ry = np.array([[np.cos(y), 0, np.sin(y)], [0,1,0], [-np.sin(y), 0, np.cos(y)]])
    Rz = np.array([[np.cos(z), -np.sin(z), 0], [np.sin(z), np.cos(z), 0], [0,0,1]])

    return np.mat(Rz)*np.mat(Ry)*np.mat(Rx)

def applyrot(R,x,y,z,x0=0,y0=0,z0=0):
    xr=np.zeros(x.shape)
    yr=np.zeros(y.shape)
    zr=np.zeros(z.shape)

    for k,val in enumerate(y):
        p0=np.mat([x[k]-x0,y[k]-y0,z[k]-z0])
        pr=R*p0.T # do rotation
        xr[k]=pr[0]+x0
        yr[k]=pr[1]+y0
        zr[k]=pr[2]+z0

    return xr,yr,zr

# Test x rotation

#Define a parabola in the z-x plane:
x=np.linspace(-10,10,100)
y=np.linspace(0,0,100)
z=x**2+y**2.

xrot45,dum,zrot45=applyrot(rotmat(45,0,0),x,y,z)
xrot90,dum,zrot90=applyrot(rotmat(90,0,0),x,y,z)
xrot180,dum,zrot180=applyrot(rotmat(180,0,0),x,y,z)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x,z, label='non-rotated')
ax.plot(xrot45,zrot45, label='rotated 45$^\circ$')
ax.plot(xrot90,zrot90, label='rotated 90$^\circ$')
ax.plot(xrot180,zrot180, label='rotated 180$^\circ$')
ax.set_xlabel('$x$',fontsize=16)
ax.set_ylabel('$z$', fontsize=16)
ax.set_title('Rotation of $z-x$ parabola in $x$',fontsize=16)
legend=ax.legend(loc='upper right', shadow=True, fontsize=12)
frame=legend.get_frame()
plt.savefig('figures/rotation_test_x.png', format='png', dpi=100)
plt.show()

# Test y rotation

#Define a parabola in the y-z plane:
x=np.linspace(0,0,100)
y=np.linspace(-10,10,100)
z=x**2+y**2.

dum,yrot45,zrot45=applyrot(rotmat(0,45,0),x,y,z)
dum,yrot90,zrot90=applyrot(rotmat(0,90,0),x,y,z)
dum,yrot180,zrot180=applyrot(rotmat(0,180,0),x,y,z)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(y,z, label='non-rotated')
ax.plot(yrot45,zrot45, label='rotated 45$^\circ$')
ax.plot(yrot90,zrot90, label='rotated 90$^\circ$')
ax.plot(yrot180,zrot180, label='rotated 180$^\circ$')
ax.set_xlabel('$y$',fontsize=16)
ax.set_ylabel('$z$', fontsize=16)
ax.set_title('Rotation of $y-z$ parabola in $y$',fontsize=16)
legend=ax.legend(loc='upper right', shadow=True, fontsize=12)
frame=legend.get_frame()
plt.savefig('figures/rotation_test_y.png', format='png', dpi=100)
plt.show()

# Test z rotation

#Define a parabola in the x-y plane:
x=np.linspace(0,0,100)
z=np.linspace(-10,10,100)
y=x**2+z**2.

dum,yrot45,zrot45=applyrot(rotmat(0,0,45),x,y,z)
dum,yrot90,zrot90=applyrot(rotmat(0,0,90),x,y,z)
dum,yrot180,zrot180=applyrot(rotmat(0,0,180),x,y,z)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(z,y, label='non-rotated')
ax.plot(zrot45,yrot45, label='rotated 45$^\circ$')
ax.plot(zrot90,yrot90, label='rotated 90$^\circ$')
ax.plot(zrot180,yrot180, label='rotated 180$^\circ$')
ax.set_xlabel('$z$',fontsize=16)
ax.set_ylabel('$y$', fontsize=16)
ax.set_title('Rotation of $x-y$ parabola in $z$',fontsize=16)
legend=ax.legend(loc='upper right', shadow=True, fontsize=12)
frame=legend.get_frame()
plt.savefig('figures/rotation_test_z.png', format='png', dpi=100)
plt.show()

# Now test rotation in y for a parabola in the z-x plane


#Define a parabola in the y-z plane:
x=np.linspace(-10,10,100)
y=np.linspace(0,0,100)
z=x**2.+y**2.

xrot45,yrot45,zrot45=applyrot(rotmat(0,45,0),x,y,z)
xrot90,yrot90,zrot90=applyrot(rotmat(0,90,0),x,y,z)
xrot180,yrot180,zrot180=applyrot(rotmat(0,180,0),x,y,z)


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(x,y,z, label='non-rotated')
ax.plot(xrot45,yrot45,zrot45, label='rotated 45$^\circ$')
ax.plot(xrot90,yrot90,zrot90, label='rotated 90$^\circ$')
ax.plot(xrot180,yrot180,zrot180, label='rotated 180$^\circ$')
ax.set_xlabel('$x$',fontsize=16)
ax.set_ylabel('$y$', fontsize=16)
ax.set_zlabel('$z$', fontsize=16)
ax.set_title('Rotation of $z-x$ parabola in $y$',fontsize=16)
legend=ax.legend(loc='center left', shadow=True, fontsize=12)
frame=legend.get_frame()
plt.savefig('figures/rotation_test_y_3d.png', format='png', dpi=100)
plt.show()



"""
#Define a parabola in the y-z plane:
x=np.linspace(-10,10,100)
y=np.linspace(0,0,100)
X,Y=np.meshgrid(x,y)
Z=X**2.+Y**2.

xx=np.ravel(X)
yy=np.ravel(Y)
zz=np.ravel(Z)

dum,dum,zrot45=applyrot(rotmat(0,45,0),xx,yy,zz)
dum,dum,zrot90=applyrot(rotmat(0,90,0),zz,yy,zz)
dum,dum,zrot180=applyrot(rotmat(0,180,0),xx,yy,zz)

sh=X.shape
zrot45=np.reshape(zrot45,sh)
zrot90=np.reshape(zrot90,sh)
zrot180=np.reshape(zrot180,sh)

fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot_surface(X,Y,Z, label='non-rotated')
ax.plot_surface(X,Y,zrot45, label='rotated 45$^\circ$')
ax.plot_surface(X,Y,zrot90, label='rotated 90$^\circ$')
ax.plot_surface(X,Y,zrot180, label='rotated 180$^\circ$')
#plot
ax.set_xlabel('$x$',fontsize=16)
ax.set_ylabel('$y$', fontsize=16)
ax.set_zlabel('$z$', fontsize=16)
ax.set_title('Rotation in $y$',fontsize=16)
#legend=ax.legend(loc='upper right', shadow=True, fontsize=12)
#frame=legend.get_frame()
plt.savefig('figures/rotation_test_y_3d.png', format='png', dpi=100)
plt.show()
"""
