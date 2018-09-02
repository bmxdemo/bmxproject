## July 02, 2018: S-21 Lab Measurements of Assembled Amp Chains

On July 2nd, 2018, I measured the S21  parameter on the amplifier chains that I
constructed using the VNA. The chain consists of:  Low Noise Amplifier, High
Pass FIlter (VHF-1080+), Low Pass Filter (VLF-1400+), Low Noise Amplifier, 
Low Pass Filter (VLFX-1350), Stage 3 Amplifier, Band Pass Filter.

I also added 60 DBs of attenuation to the front of the chain in order to avoid
overloading the third amplifier. The measurements were taken at -35 DBs into the 
chain and with a supplying DC voltage of 3 volts. 

We can compare these measurements to 
[Amplifier S21 data previously collected ](../20180410_New_Amps_S21/index.md). 
~~The data looks to be consistent with what we would expect of the amplifier
chains, and indicated that they are working as expected.~~
The original data had a few more DBs than expected, but this was solved by
realizing that I did not calibrate the VNA before taking the original data. We
were originally concerned that the data was not centered at 0, but we realized
that it was just the differnce in the noise floor and was likely a red
herring. The updated data is below.

### S21 Measurements

![Picture](Amptest2018.png)