
## RFI Rejection Tests

Data chunks of size 2^20 are flagged as RFI if their variance is an outlier among the variances of neighboring chunks. 
Test data was collected in the basin between 7/18/17 and 7/20/17. 


### RFI Density
The following is a plot of RFI density over 16 hours from 8:00 PM, July 18 - 12:00 PM, July 19

![trace](RFIDensity170718_2200-170719_1100_4sigma.png)

The following is a plot of RFI density over 15 hours from 12:00 AM, July 20 - 3:00 PM, July 20
![trace](RFIDensity170720_0000-170720_1400_5sigma.png)

Here are the two time streams overlayed on one plot:
![trace](RFIOverlayDensity.png)

### RFI Frequency
Taking the FFT of the outlier density data gives the following power spectra. Note that the two timestreams display similar peaks at around 2 and 3.7 Hz.

####  8:00 PM, July 18 - 12:00 PM, July 19
Every 1000 frequencies are binned and averaged together:
![trace](RFIFrequency170718_2200-170719_1100_4sigma.png)

No binning:
![trace](RFIFrequency170718_2200-170719_1100_4sigma_unbinned.png)

Log scale on the x axis:
![trace](RFIFrequency170718_2200-170719_1100_4sigma_unbinned_logx.png)

#### 12:00 AM, July 20 - 3:00 PM, July 20
Every 1000 frequencies are binned and averaged together:
![trace](RFIFrequency170720_0000-170720_1400_5sigma.png)

No binning:
![trace](RFIFrequency170720_0000-170720_1400_5sigma-unbinned.png)

Log scale on the x axis
![trace](RFIFrequency170720_0000-170720_1400_5sigma-unbinned_logx.png)



### RFI Waveforms and Power Spectra
The following is a randomly selected sample from the flagged chunks. Displayed are the waveform and power spectrum for each chunk:
The titles are the date and time, followed by the chunk index.



# 1)

![trace](170718_2200_57_waveform.png)
![trace](170718_2200_57_spectrum.png)

# 2)

![trace](170718_2300_113_waveform.png)
![trace](170718_2300_113_spectrum.png)

# 3)

![trace](170719_0200_576_waveform.png)
![trace](170719_0200_576_spectrum.png)

# 4)

![trace](170719_0400_1111_waveform.png)
![trace](170719_0400_1111_spectrum.png)
# 5)

![trace](170719_0500_0_waveform.png)
![trace](170719_0500_0_spectrum.png)

# 6)

![trace](170720_0200_0_waveform.png)
![trace](170720_0200_0_spectrum.png)

# 7)

![trace](20_4_170718_2200_111_waveform.png)
![trace](20_4_1701718_2200_111_fft.png)






