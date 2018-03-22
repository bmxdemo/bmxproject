## March 22, 2018 - Recent Changes to Experimental Configuration
### Changes from 180314:

Following the revelation that our odd frequency blobs are in fact transiting
satellites, we discussed returning to a more aggressive configuration of the
amplifier chain. The goal was to ensure that placing the first band pass filter
behind the first LNA was not going to have unintended consequences from
amplifying out of band terrestrial signals. To test this, I used the USB power
meter to measure the power of the sky signal from 1MHz to 8.0GHz after being
amplified by the first LNA, and found that it was below -40dBm, as the signal
was below the minimum threshhold of the power meter. Due to geometric
limitations of the channel 2 (Y-pol) amplifier chain, I was unable to place the
first band pass immediately after the first LNA, so I opted to place it after
the second LNA. Using the power meter after the second amplifier also failed to
meet the minimum threshhold. I concluded that these power levels after
filtration were satisfactory for amplifier performance.

Because we no longer needed to accomodate a band pass in front of the first
amplifier, we could remove many components from the front of the amplifier
chains. Additionally, we wished to return to the noise diodes to the couled
ports of the OMT, therefore I removed the 30dB coupler and the second low loss
cable, minimizing the number of components and connections before the first
amplifier. In order to supply a calibration signal to both amplifier chains, I
soldered a second noise diode to a spliced BNC cable, which connects to the 28V
regulated supply. There is a PE85N1000 calibrated noise source on both channels,
which supplies 15dB ENR.

As of 180314_2145, the configuration of the amplifier chains were as follows:

~~~
Channel 1 - X-pol - Vetical
  -------------------------
  OMT+Horn
  -------------------------
  Low-Loss Cable
  LNA 1
  Band Pass Filter 1	
  3dB Attenuator
  LNA 2	
  Low Pass Filter (VLFX-1350)
  Stage 3 Amplifier
  Front End Output Port
  _________________________
  Band Pass Filter 2
  Data Cable
  -------------------------

Channel 2 - Y-pol - Horizontal
  -------------------------
  OMT+Horn
  -------------------------
  Low-Loss Cable
  LNA 1	
  3dB Attenuator
  LNA 2	
  Band Pass Filter 1
  Low Pass Filter (VLFX-1350)
  Stage 3 Amplifier
  Front End Output Port
  _________________________
  Band Pass Filter 2
  Data Cable
  -------------------------
~~~

The data acquisition ran for 5 days in this configuration, before we discussed
making further changes at the group meeting on Tuesday. The most noticable
difference in the data following these changes is the height of the diode pulse,
which is due to the difference in S21 of the 30dB coupler as compared to the OMT
coupled ports. To rectify the calibration methods applied by the BMX data
browser, I will have to take new S21 measurements with the VNA, which
unfortunately couldn't be completed on 180320. 

### Changes from 180320:

Following the latest group meeting and BMX discussion meeting, changes were
proposed for the amplifier chain once more. I removed the first band pass filter
from both channels, and replaced it with a combination of low pass and band pass
filters which would emulate the filtration supplied by the expensive band
pass. In addition, because these filters are smaller than the band pass, I was
able to place the entire amplifier chain inside the front end enclosure, after
removing the 3dB attenuator. 

The configuration is now standardized on both channels, as follows:

~~~
Both Channels:
  -------------------------
  OMT+Horn
  -------------------------
  Low-Loss Cable
  LNA 1
  High Pass FIlter (VHF-1080+)
  Low Pass Filter (VLF-1400+)
  LNA 2	
  Low Pass Filter (VLFX-1350)
  Stage 3 Amplifier
  Band Pass Filter
  Front End Output Port
  _________________________
  Data Cable
  -------------------------
~~~

The calibration ports on the OMT are somewhat difficult to work with when the
OMT is installed, but in the next several days I will attempt to adjust the
depth of the coaxial cable to attain S21 of approximately 30dB. This should
adjust the height of the diode pulse to more reasonable levels, as seen before
these hardware changes.