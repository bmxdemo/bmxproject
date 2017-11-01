## Nov 1, 2017 - Damaged Digitizer Card Ports

### Palantir 2 Channel Card Status:

Some time within the past few weeks, I damaged the SMA connections that are
soldered to the digitizer card. I clearly failed to properly connect the cables,
and then damaged the connectors by securing the nuts.

The card is the 2 channel digitizer card, which only had one stable channel (chan1). We
believe that one of the (chan 2) ADCs is not properly functioning, and is causing the
gain to fluctuate when we restart the data acquisition.

Only channel 1 is operational for looking at sky data, and data has been
collected from 10/24/17 to today, 11/1/17. 

### (10/24 - 10/26) 

The data acquisition was as before, taking 1000 samples (2min) of data
repeatedly, and restarting the data acquisition after each file. We observe that
the system was relatively stable in the current configuration with the noise
diode mounted via 30dB coupler.

There are some stability issues observed in this data but a more obvious
example will be discussed later.

**Figure 1: Time Series of Sky Signal on Channel 1**
![Sky](TimeSeries_1024_1027.png)

### (10/28-10/29)

We wanted to further pin down a faulty ADC as the culprit behind the gain
switching, but in the process of conducting that test, I noticed the damaged
ports on the digitizer card. Progress was halted, and the computer was returned
to the physics building.

This image was sent around by email, and shows the damage to the digitizer card:

**Figure 2: Impacted Ports**
![1](image1.JPG)

The impacted ports were opened back up using a round tipped set of tweezers, to
delicately push the petals apart. 

**Figure 3: 'Repaired' Ports**
![2](image2.JPG)

The data acquisition ran for the next few days on hour long samples, and
appeared relatively stable, but there are still problematic switches that show a
change in pulse height.

**Figure 4: Time Series for Hour Samples (10/28-10/29)**
![hour](TimeSeries_ch1_1028_1029.png)

And here is the aforementioned pulse height change, from the first noticeable
change in the power:

**Figure 5: Pulse Height Change**
![PH](PHChange_1028.png)

And this is the file in question, from 0900:

**Figure 6: Jumping Time Series Power**
![jump](TSjump1028.png)

I am investigating the change in the spectra from this time. They are
essentially unrecognizable from the spectra taken a week ago.

**Figure 7: Junk Spectra**
![junk](junkspec.png)

### More of the Same

Looking at the data from the past two days, it is obvious that this erratic
behavior is continuing, and the data is not reliable. the shape of the spectra
is not in keeping with what we saw before, and I suspect the damage to the
digitizer card is the reason why. 

I think we need to replace the card or the PC before we can again take
meaningful data.

**Figure 8: More Unstable Behavior**
![spooky](TimeSeries_1030_1031.png))