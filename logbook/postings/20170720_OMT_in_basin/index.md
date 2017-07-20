### July 20 2017 - OMT in the basin

A Slosar

### Setup

The basic purpose of this experiment was to do some measurements for
Chandler, but also just test the entire setup including network
connectivity, aux data aquisition, etc.

The setup at the end of Wednesday was something like this:

|![alt-text](../20170720_OMT_in_basin/a1.jpg)|
|![alt-text](../20170720_OMT_in_basin/a2.jpg)|
|![alt-text](../20170720_OMT_in_basin/a3.jpg)|


OMT was pointing straight up, both channels were connected, taking
data at 1.1GHz sampling with both channels connected to the digitizer
(I believe for the first time). The two channels has marginally
different set-up -- one had an attenuator rather than first filter
between amps. But otherwise the set up was exactly the same.

# Webcam data

We were taking webcam data throughout. Two intesteresting movies on
the second day (two file reaquisition starts at midnight):

[CAM1](https://www.dropbox.com/s/pqpn1qaohmtmjei/170720_0000_cam0.avi?dl=0)
[CAM2](https://www.dropbox.com/s/q7gl47m746vj4ba/170720_0000_cam1.avi?dl=0)


# Temperature data

The temperature sensors were running too:

|![alt-text](../20170720_OMT_in_basin/temp.png)|

Clearly the temperatures >50 seems suspiciously high even though they
were under the sun. We need more sensible timestamping too, but it basically workse.

# Connectivity

Connectivity was fine, getting sustaing 7Mb transfers to astro cluster


# Data

Data were  taken with  RFI filtering  with 0.95ms  chunks and  4 sigma
rejection.  All   the  rejected   samples  were  saved.   This  caused
uncontrolled   increased   in   file   sizes  that   filled   up   the
disk. Therefore, we have data overnight from 7pm to 11AM on first day,
some daylight data with long interruptions  and then data 9PM - 2PM on
the second day.


The first look at the data shows large variations across frequency,
which could be RFI, but are too broad in my opinion.  Both channels
give similar results. We seem to clearly see a signal bleeping every
15s consistent with radar contamination.  We also see a massive drop in the detected RFI events 
over night with the bottom at around 2-3AM. Hindy and Chandler will
update this logbook as the first look analysis progresses.

We also took separate data for measuring acryllic stuff. CC will
report on that.
