# coding: utf-8
import healpy as hp
import matplotlib.pyplot as plot
import numpy as np
import cPickle

with open("cosmo_sdss.pickle", "rb") as f:
    maplist = cPickle.load(f).streams[0]

z_list = [(1420 - i) / i for i in np.arange(1100.25, 1420.25, 0.5)]

split_list = []

j = 0
for i in np.arange(0.290, 0, -0.001):
    while z_list[j] > i:
        j += 1
    split_list.append(j)

new_maplist = []

prev_i = 0
for i in split_list:
    row = np.mean(maplist[prev_i:i], axis=0)
    new_maplist.append(row)
    prev_i = i

row = np.mean(maplist[i:], axis=0)
new_maplist.append(row)
new_maplist = np.vstack(new_maplist)

plot.imshow(new_maplist, cmap="gray_r", interpolation="nearest", aspect="auto", extent=(100, 280, z_list[-1], z_list[0]))
plot.xlabel("RA")
plot.ylabel("z")
plot.title("12-hour simulation output")
plot.savefig("sdss_corr.png")
