# coding: utf-8
import healpy as hp
import matplotlib.pyplot as plot
import numpy as np

def read_map(num):
    a = hp.read_map("/astro/u/anze/work/BMX/CRIME/output/colore__imap_s1_nu%03d.fits" % num)
    proj = hp.projector.GnomonicProj(rot=(-170, 40.8, 0), coord=["G", "C"], xsize=180, ysize=4, reso=60)
    vec2pix = lambda x, y, z: hp.vec2pix(Nside, x, y, z)
    Nside=512
    pmap = proj.projmap(a, vec2pix)
    return np.mean(pmap, axis=0)

if True:
    print(read_map(0).shape)
    maplist = np.vstack([read_map(i) for i in range(639)])
    print(maplist.shape)
    extent = (100, 280, (1420 - 1100.25) / 1100.25, (1420 - 1419.75) / 1419.75)

    np.save("maplist.npy", maplist)

else:
    maplist = np.load("maplist.npy")

z_list = [(1420 - i) / i for i in np.arange(1100.25, 1420.25, 0.5)]


# z value is not linear with frequency, so stretch the map to be linear with z value
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
plot.title("colore map projection 38.8 < dec < 42.8")
plot.savefig("sdss_corr.png")
