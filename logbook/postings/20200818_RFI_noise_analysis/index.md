Jesse Osborn, August 18th, 2020

# **RFI Noise Analysis**

From July 8th to August 17th, Dr. Slosar and I have been investigating the RFI noise spikes present in the data, and I have developed a few ways for partially removing them from the data. Currently, there are two functions, remove_spikes_V1 and remove_spikes_V4, that can be run over the data. Version 1 runs over each individual d[xxy] plot, finds narrow spikes, and replaces every point in the narrow spikes (above a given threshold) wth np.nan. By contrast, version 4 runs over each d[xxy].mean(axis=0), finds narrow spikes, and then goes back through every d[xxy] plot and removes the spikes there, as in version 1.

Version 1 seems to be more successful in removing all narrow spikes (large and small, on top of good data and not) from the data, but it takes orders of magnitude longer than Version 4 to run (since it scans every d[xxy] plot) and it seems to leave a very slight "undercutting" of the baseline of data. Version 4, however, runs very quickly and removes most of the narrow spikes. The version 4 spike finder may require more complexity in its scanning of data plots in order to remove all of the spikes, perhaps making use of more than the one threshold in use now (in order to catch tall spikes hidden in the good data as well as very short spikes close to the baseline).

We have also worked on analysing the diode pulses that are seen in the data and their relation to the gain effects seen in the data. The results of this analysis are given at the beginning of the remove_spikes_V4.ipynb Jupyter notebook.

The up to date code for this investigation can be found in **https://github.com/bmxdemo/bmxhacks** for the two Jupyter notebooks, remove_spikes_V1.ipynb and remove_spikes_V4.ipynb, and **https://github.com/bmxdemo/bmxobs** (jesseO_branch currently), for the bmxobs setup code for the two Jupyter notebooks.
