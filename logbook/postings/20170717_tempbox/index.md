### July 17 2017 - Temperature in the box

A Slosar

### Setup

Put computer in a box together with 1-wire temperature sensors and
taped it all around to make it as thermaly insulated as possible to
see how far we can push this. In practice we expect things to be
ventilated through holes.

|(./p1.jpg)|(./p2.jpg)|


Sensor 1 was put at the exhaust of computer's fan, Sensor 2 in a
random corner of the box. The computer ran for overnight and reached
steady state after a few hours. We ran a full data acquisition with
RFI rejection, etc. In the morning, the acquisition was stopped, which
cased the suddent drop in temperature.

The temperature plot looks as follows:

|(./temp.png)|

Even though it was cooking, the computer was running just fine with no
alarams or warnings in the log. Occasionally it pays to buy a server
room grade motherboard.
