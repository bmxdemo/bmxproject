### ADC Synchronization part 2:

Hindy Drillick

In my [last post](../20180303_ADC_Synchronization/index.md), we were seeing a 
wide range of delays from -20 to 20 ms between the signal received by each of the two cards. 

Starting up DAQ requires passing multiple flags to the digitizer card. We were initially 
passing the following 3 flags in one function call:

1. M2CMD_CARD_START - this flag starts up the card
2. M2CMD_CARD_ENABLE_TRIGGER - any subsequent trigger event will now be recognized 
3. M2CMD_CARD_START_DMA - starts the memory transfer

However, since it takes a while to start up the card (the first flag), the two 
cards had their triggers enabled at different times, which caused significant delays.
To solve this, I split the flags into separate function calls, and threaded them,
so that the calls are made concurrently for each card. 

This solves most of the issues. Instead of having a wide spread of delay values, we 
now see an extremely small delay (< .1 ms) in most cases. However, in some cases, we  
have a delay with the very specific value of 11.9 ms. It  
seems that this 11.9 ms delay has to do with the testing method, as proccessing the raw 
data takes longer than the actual DAQ cycle. The prevalence and size of this delay also 
depends on the size of the buffer multiplier, which is the size of the buffer in PC memory as  
a multiple of one cycle of data. 

The following is a histogram of delays between the two cards obtained from running
DAQ 1000 times with a pulse modulated signal. I then calculated the time difference 
between pulse edges in the digitizer output for both cards.

![Image]
(../delays_hist.png)

mean: 0.77120848601 \
std: 2.95830176192 \
min: -0.095977273 \
max: 11.964425455

Since most of the delays cluster around zero, the following is a zoomed in plot of
just those values.

![Image]
(../delays_hist_cropped.png)

## Conclusion: 
It seems that the two cards are synchronized within .1 ms of each other.                                                                                      
