import numpy as np
import sys,os

# This code takes the xyz.txt output from PhotoModeler
# and sorts the data set by the Point ID values in the 
# first column.  It also removes any points that define
# the axes from the list.

# Usage:
# python sort_photomodeler_output.py xyz.txt

points=np.loadtxt('data/'+str(sys.argv[1]))
#points=np.array((points))


# Frist sort data
points=points[points[:,0].argsort()]

# Now remove points defining axes
# We do this be removing any rows containing a value of
# zero for either x, y, or z.
to_remove=[i for i,val in enumerate(points) if val.all() == 0]
for index in reversed(to_remove):
    points=[val for i,val in enumerate(points) if i != index]

# Output new xyz.txt and overwrite old
np.savetxt('data/'+str(sys.argv[1]), points, delimiter='    ')
