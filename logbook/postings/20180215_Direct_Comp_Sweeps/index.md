## Feb 15, 2018 - Direct Comparison of Bench & Basin RFI Environments
### Motivation: Too Many Unstable Parameters!

Over the past several weeks, I have attempted to perform frequency sweep tests
both on the bench and in the basin, and the results have been rather
inconsistent. The goal was to examine the response of our OMT/Amplifiers/Filters
to a low frequency sweep at high power, specifically looking for power mixing
and intermodulation products appearing within the band. 

### Experimental Configuration:

These frequency sweeps were all performed using the Spartant signal generator
(with 2 Low Pass filters on the RF output, to attenuate high frequency harmonics
by ~80dB,) locked to the 10MHz signal output by a lab signal generator  which
also clocked the ROACH FPGA. The frequency sweeps were all performed from 25MHz
- 600MHz with a 1MHz step, at a power of +13dBm. To keep our system consistent,
I performed these tests using the amp chain I constructed on the bench, with a
2.9V supply. The amp chain is arranged as it has been in the past, and is
identical to the amp chain on the bench:

~~~
  -------------------------
  OMT/Terminator/Spartant+2LP
  -------------------------
  Band Pass Filter 1
  LNA 1 	
  3dB Attenuator
  LNA 2	
  Low Pass Filter (VLFX-1350)
  Stage 3 Amplifier
  [**When OMT, attach 10dB Attenuator**]
  _________________________
  ROACH FPGA
  -------------------------
~~~

These tests were first conducted on the bench, and then in the basin. The
fundamental setup was the same. First, I performed a direct injection of the
frequency sweep from the signal generator directly into the amp chain. Second, I
terminated the amp chain and broadcast the frequency sweep through the log
periodic, looking for direct coupling to the amp chain components. Finally, I
connected the OMT (from the lab) into the amp chain, and broadcast the frequency
sweep directly into the OMT.

**Figure 1: 180215 Experimental Configuration in Basin:**
![setup](IMG-3033.JPG)

The difference between these tests were limited to the physical location (and
hence RFI environment,) and the receiver. 

### Test Results: Waterfall Plots

**Figure 2: 180215 Bench Injection Test:**
![BeI](180215_Bench_Injection.png)

**Figure 3: 180215 Bench Terminated Broadcast Test:**
![BeT](180215_Bench_Terminated_Broadcast.png)

**Figure 4: 180215 Bench OMT Broadcast Test:**
![BeO](180215_Bench_OMT_Broadcast.png)

**Figure 5: 180215 Basin Injection Test:**
![BaI](180215_Basin_Injection.png)

**Figure 6: 180215 Basin Terminated Broadcast Test:**
![BaT](180215_Basin_Terminated_Broadcast.png)

**Figure 7: 180215 Basin OMT Broadcast Test:**
![BaO](180215_Basin_OMT_Broadcast.png)

### Summary:

~~~
180215 BENCH INJECTION	—> mild fundamental, in band visible 2nd and 3rd Harmonics (5e7,1e9)
180215 BENCH TERMINATED	—> Low frequencies: fund, 2nd, 3rd, 4th, 5th harmonics
			   In Band, no response
			   High frequencies: power reduction, black lines mirroring low freq
180215 BENCH OMT	—> Junk at t~0 and t~700 is from me entering and leaving the room
			   Fundamental and 2nd harmonic in low frequency range
			   No features evident in band?? (1e9,1e11)
180215 BASIN INJECTION	—> mild fundamental, in band visible 2nd and 3rd Harmonics (5e7,1e9)
180215 BASIN TERMINATED	—> Low frequencies: fund, 2nd harmonics
			   In Band, no response to broadcast signal (1e8,5e9)
			   High frequencies: very faint black mirror of fund (5e5,1e8)
180215 BASIN OMT	—> strong fundamental, visible 2nd harmonic below band
			   In band: visible 1st, 2nd, 3rd, …, 9th? Harmonic visble
~~~

