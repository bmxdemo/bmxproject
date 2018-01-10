# Generating CRIME and CoLoRe maps for bmxsim [AS, 10 Jan 2018]

## Cookbook

We use the CRIME package to generate foreground maps using `ForGeT`
software. This is non-parallel software that takes a lot of memory but
essentially generates correlated Gaussian fields with some correlation
length that change both in frequency and space. See
[Crime website](http://http://intensitymapping.physics.ox.ac.uk/CRIME.html).


Use CRIME compiled in `/astro/u/anze/work/BMX/CRIME`. 
Run 
```
py/makeNuTable.py ## generate list of frequencies
./ForGet ini/param_ForGet_egfree.ini #extra-galactic free-free
./ForGet ini/param_ForGet_gfree.ini #galatcic free-free
./ForGet ini/param_ForGet_gsync.ini #galactic synchrotron
./ForGet ini/param_ForGet_psources.ini # radio point sources
```

The last one is for sources, which we will eventually replace with
properly correlated sources.

Use CoLoRe (general purpose code derived from Crime) in
`/astro/u/anze/work/LSST/CoLoRe`. 

Execute

```
bash runbmx
```
which submits a job to the cluster using `bmx.cfg`. The later should
be self explanatory

## Quality assurance

See [here](./mapcheck.ipynb) for python notebook with some code.

In particular:
 * Some artifacts are still seen at low-z, but they should affect
   anything after accounting for our beam
 * Note the filename convention. The CRIME indices run from 1-640, the
   CoLoRe indices run from 639-0. 
 * Sources are packed in the same number of files as processors
   used. This is how you read them in
   `srcs=np.hstack([pf.open(outdir+'/colore__srcs_s1_%i.fits'%i)[1].data
   for i in range(16)])`
   which gives you a numpy array with `RA`, `DEC`,`Z_COSMO`,`DZ_RSD`
   fields
   
