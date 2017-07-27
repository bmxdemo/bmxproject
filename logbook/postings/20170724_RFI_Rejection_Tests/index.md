
### RFI Rejection Tests

Data chunks of size 2^20 are flagged as RFI if their variance is an outlier among the variances of neighboring chunks. 
Test data was collected in the basin between 7/18/17 and 7/20/17. 

The following is a plot of RFI density over 16 hours from 8:00 PM, July 18 - 12:00 PM, July 19

![trace](RFIDensity170718_2200-170719_1100_4sigma.png)

The following is a plot of RFI density over 16 hours from 12:00 AM, July 20 - 2:00 PM, July 20
![trace](RFIDensity170720_0000-170720_1400_5sigma.png)

Taking the FFT of the outlier density data gives the following power spectra. Note that the two timestreams display similar peaks at around 2 and 3.7 Hz.

![trace](RFIFrequency170718_2000-170719_1100_4sigma.png)
![trace](RFIFrequency170720_0000-170720_1400_5sigma.png)




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






