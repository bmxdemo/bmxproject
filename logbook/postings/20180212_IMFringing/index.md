## Feb 12, 2018 - Intermodulation fringing (AS)

I took the 180210_1400 data file that has a nice transiting source.
CH1 was in the inverted state, CH2 was fine.
I did zero calibration and completelly ignored calibration diode pulses (ie. just ignored them).
Averaged the data x4 in freq direction and x64 in time direction.

The plot below shows frequencies where our intermodulation appears. The top plots are auto-power for
CH1 and CH2 and the bottom plot is the amplitude and phase of cross-power.

![fr1](./fr1.png)

Look at the structure around sources.

The plot below show the cross-correlation coefficient
|PX|/sqrt(P1*P2):

![fr2](./fr2.png)

So, it is approaching one, so I think what we are seeing is fully correlated signal, but r is a bit less then unity due to noise.

The plot blow shows a slice for a particular freuqency bin. Here I
show the real and imaginary part of cross. It is clear here that the
phase is wrapping and the overal signal is modulated by the source.

![fr3](./fr3.png)


The final plot shos the phase as a function of frequency. It is the
same information as plotted on bottom right of Fig1, but plotted
differently.

![fr4](./fr4.png)

Note that for a perfect single-dish experiment the cross-power should
be U+iV. Interferometry on the other hand gives
`P0*exp(i*phi*D/lambda)`, and we are clearly phenomenologically closer
to the latter. What is clear is that whatever is causing this
intermodulation knows about where on the sky source is.
