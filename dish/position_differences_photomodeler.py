import numpy as np
import sys,os
import matplotlib.pyplot as plt

# This code takes two sets of xyz.txt outputs
# from PhotoModeler and finds the difference
# between the two arrays.  The assumption is that
# both xyz.txt data sets refer to two different
# measurements (two different sets of photographs)
# of the same object.  The difference in arrays therefore
# gives an estimate of the measurement uncertainty 
# one can expect from using PhotoModeler.

# Usage:
# python position_differences_photomodeler.py xyz_1.txt xyz_2.txt

points1=np.loadtxt('data/'+str(sys.argv[1]))
points2=np.loadtxt('data/'+str(sys.argv[2]))

# Get x coordinates in mm
x1=points1[:,1]*1e3
x2=points2[:,1]*1e3

# Get y coordinates in mm
y1=points1[:,2]*1e3
y2=points2[:,2]*1e3

# Get z coordinates in mm
z1=points1[:,3]*1e3
z2=points2[:,3]*1e3

print 'The x differences in mm are',x1-x2
print 'The y differences in mm are',y1-y2
print 'The z differences in mm are',z1-z2

# Plot some histograms

fig=plt.figure()
ax=fig.add_subplot(111)
ax.hist(x1-x2)
ax.set_xlabel('$x_1-x_2$ [mm]',fontsize=16)
ax.set_ylabel('Number of data points', fontsize=16)
ax.set_title('Differences in $x$ coordinates of the two data sets',fontsize=16)
plt.savefig('figures/'+str(sys.argv[1])+'-'+str(sys.argv[2])+'_x_differences_histogram.png', format='png', dpi=100)
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
ax.hist(y1-y2)
ax.set_xlabel('$y_1-y_2$ [mm]',fontsize=16)
ax.set_ylabel('Number of data points', fontsize=16)
ax.set_title('Differences in $y$ coordinates of the two data sets',fontsize=16)
plt.savefig('figures/'+str(sys.argv[1])+'-'+str(sys.argv[2])+'_y_differences_histogram.png', format='png', dpi=100)
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
ax.hist(z1-z2)
ax.set_xlabel('$z_1-z_2$ [mm]',fontsize=16)
ax.set_ylabel('Number of data points', fontsize=16)
ax.set_title('Differences in $z$ coordinates of the two data sets',fontsize=16)
plt.savefig('figures/'+str(sys.argv[1])+'-'+str(sys.argv[2])+'_z_differences_histogram.png', format='png', dpi=100)
plt.show()
