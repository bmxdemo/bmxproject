
import numpy as np
import os
import glob
from matplotlib.pyplot import *


folder = '/direct/astro+u/lberkhou/bmxproject/logbook/postings/20180702_amp_chain_S21'
os.chdir(folder)
filenames = glob.glob('*.csv')

dat1 = np.genfromtxt('20180702_silver_chain1.csv', delimiter=',')
dat2 = np.genfromtxt('20180702_black_chain2.csv', delimiter=',')

Atten = 60
## FULL RANGE OF VNA
figure(1)
subplot(1,2,1)
plot(dat1[1:,0]*(1/1e6),dat1[1:,1]+Atten, label='Amp Chain 1')
plot(dat2[1:,0]*(1/1e6),dat2[1:,1]+Atten, label='Amp Chain 2')
grid()
title('S21 Measurements of Full Amplifier Chain')
xlabel('Frequency, $MHz$')
ylabel('S21, $dB$')
xlim(-50,4850)
ylim(-40,80)
legend()
## ZOOM OVER BAND
subplot(1,2,2)
plot(dat1[1:,0]*(1/1e6),dat1[1:,1]+Atten, 'b', label='S21 Amp 1')
plot(dat2[1:,0]*(1/1e6),dat2[1:,1]+Atten, 'g', label='S21 Amp 2')
grid()
title('S21 Measurements of Full Amplifier Chain')
xlabel('Frequency, $MHz$')
ylabel('S21, $dB$')
xlim(1000,1700)
ylim(0,80)
legend()
savefig('Amptest.png')
