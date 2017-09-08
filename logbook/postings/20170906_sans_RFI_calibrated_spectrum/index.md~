## Sep 06, 2017: Calibrated Spectra - Reduced RFI


On Aug 30, 2017, Chris had a revelation: the amps were being driven non-linear
by the out of band RFI. We made several modifications to the amp chain, in order
to reduce incoming RFI. The crucial change involved moving both band pass
filters onto the same channel: one after the first amp, to reduce the total
signal being amplified, and one after the last amp to nullify the noise of the
amplifiers. The current configuration of the amp chain is as follows:

Sky -> LNA -> BP -> LNA -> Low Pass -> AMP2 -> BP -> Spectrometer

### Uncalibrated Spectra:

With the SignalHound in place of the spectrometer(PC), we collected 28 spectra
over the course of about 15 minutes. The .bbr file which contains these data is
'/gpfs/mnt/gpfs01/astro/workarea/signalhound/2017-08-24 15h36m26s.bbr' and the log of changes with loose time-stamps
can also be found in the SignalHound folder on the cluster.

To decrease noise/eliminate some time variability, we took averages over a few
 spectra.
1.  Spectra from sky
2.  Spectra with input terminated at 290K
3.  Spectra with input terminated at 77K in liquid nitrogen
![spectra](SH_spectrum_mW.png)

### Gain and Noise Floor Calculations:

Power = Gain * (Temperature) + Noise

For a given frequency, a plot of power (mW) versus temperature (K) will be a
line segment, with points at T = 290 K, and T = 77 K. The slope of this line
segment is the gain, and the y-int of the "line" is the noise from the system,
as the temperature approaches T = 0 K.

In python, Chris helped me do some very simple array operations which calculated
the gain (mW/K), and the noise (mW). The ratio n/g then yields the noise
temperature in K.

![Temp](SH_Noise_Temp.png)

### Calibrated Spectra:

Utilizing these values, we calibrate the sky spectra, over the course of a few
minutes. This was taken with the SignalHound, so each color is a different sweep. The resulting plot of sky temperature vs. frequency can be
seen below.

![calspec](SH_fig1.png)