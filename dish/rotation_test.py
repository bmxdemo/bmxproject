import numpy as np
import matplotlib.pyplot as plt

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

#Define a parabola in the x-z plane:
x=np.linspace(-10,10,100)
y=np.linspace(0,0,100)
z=x**2+y**2.

dum,dum,zrot45=applyrot(rotmat(45,0,0),x,y,z)
dum,dum,zrot90=applyrot(rotmat(90,0,0),x,y,z)
dum,dum,zrot180=applyrot(rotmat(180,0,0),x,y,z)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x,z, label='non-rotated')
ax.plot(x,zrot45, label='rotated 45$^\circ$')
ax.plot(x,zrot90, label='rotated 90$^\circ$')
ax.plot(x,zrot180, label='rotated 180$^\circ$')
ax.set_xlabel('$x$',fontsize=16)
ax.set_ylabel('$z$', fontsize=16)
ax.set_title('Rotation in $x$',fontsize=16)
legend=ax.legend(loc='upper right', shadow=True, fontsize=12)
frame=legend.get_frame()
plt.savefig('figures/rotation_test_x.png', format='png', dpi=100)
plt.show()

# Test y rotation

#Define a parabola in the y-z plane:
x=np.linspace(0,0,100)
y=np.linspace(-10,10,100)
z=x**2+y**2.

dum,dum,zrot45=applyrot(rotmat(0,45,0),x,y,z)
dum,dum,zrot90=applyrot(rotmat(0,90,0),x,y,z)
dum,dum,zrot180=applyrot(rotmat(0,180,0),x,y,z)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(y,z, label='non-rotated')
ax.plot(y,zrot45, label='rotated 45$^\circ$')
ax.plot(y,zrot90, label='rotated 90$^\circ$')
ax.plot(y,zrot180, label='rotated 180$^\circ$')
ax.set_xlabel('$y$',fontsize=16)
ax.set_ylabel('$z$', fontsize=16)
ax.set_title('Rotation in $y$',fontsize=16)
legend=ax.legend(loc='upper right', shadow=True, fontsize=12)
frame=legend.get_frame()
plt.savefig('figures/rotation_test_y.png', format='png', dpi=100)
plt.show()

# Test z rotation

#Define a parabola in the x-y plane:
x=np.linspace(0,0,100)
z=np.linspace(-10,10,100)
y=x**2+z**2.

dum,yrot45,dum=applyrot(rotmat(0,0,45),x,y,z)
dum,yrot90,dum=applyrot(rotmat(0,0,90),x,y,z)
dum,yrot180,dum=applyrot(rotmat(0,0,180),x,y,z)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(z,y, label='non-rotated')
ax.plot(z,yrot45, label='rotated 45$^\circ$')
ax.plot(z,yrot90, label='rotated 90$^\circ$')
ax.plot(z,yrot180, label='rotated 180$^\circ$')
ax.set_xlabel('$z$',fontsize=16)
ax.set_ylabel('$y$', fontsize=16)
ax.set_title('Rotation in $z$',fontsize=16)
legend=ax.legend(loc='upper right', shadow=True, fontsize=12)
frame=legend.get_frame()
plt.savefig('figures/rotation_test_z.png', format='png', dpi=100)
plt.show()


