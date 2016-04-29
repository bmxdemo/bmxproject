import visa, time , signal
import matplotlib.pyplot as plt
import numpy  as np 

plt.close('all')


###############################################################################
# User  settings
###############################################################################

sa_ip = '169.254.212.229'
freq_center = '0.5GHz'
freq_span = '1000MHz'
rbw = 100000
input_atten = 0 


delay = 0


# Plot Settings
plot_size = (12,8)
ymin1=-110
ymax1=-10

ymin2=1
ymax2=0

xAxis_Label1 = 'Freq [MHz]'
yAxis_Label1 = '[dBm / RBW]'

xAxis_Label2 = 'Freq [MHz]'
yAxis_Label2 = '[pW / RBW]'

# Number of spectra in one plot
N_spect_plot = 1000 


#Data File name and Folder 
datafile = 'RFI_BNL.txt'
folder ='C:\\Users\\hamdi\\Desktop\BNL_Project_BMX\\'

###############################################################################
# Connect to Instrument
###############################################################################
rm = visa.ResourceManager()
rm.list_resources()
fsv = rm.open_resource('TCPIP0::'+ sa_ip+ '::inst0::INSTR')
fsv.timeout = 12000 # in milliseconds 
print(fsv.query("*IDN?"))

###############################################################################
# Configure Instrument
###############################################################################
#fsv.write("*rst")
fsv.write("init:cont 0")

fsv.write("freq:center "+freq_center)
fsv.write("freq:span " +freq_span)
fsv.write("BAND:RES "+ str(rbw))
fsv.write("INPut:ATTenuation " + str(input_atten))

freq_start = float(fsv.ask("freq:start?")) / 1E6
freq_stop = float(fsv.ask("freq:stop?")) / 1E6
freq_points =float(fsv.ask("swe:points?"))
freq_MHz=np.linspace(freq_start,freq_stop,freq_points)

###############################################################################
# Acquire Data function 
###############################################################################
def Acquire_Data():
    date_time_string= time.strftime('%m%d%Y %H:%M:%S')
    print('Triggering a new Sweep...')
    fsv.ask("*trg;*opc?")
    print('Waiting for the sweep to finish...')
    y = fsv.ask("trac:data? trace1")
    print('Downloading data ...')
    y.rsplit(',')
    trace =[]
    for i in range(len(y.rsplit(','))):
        trace.append(float(y.rsplit(',')[i]))
    return trace , date_time_string

def Plot_Data(trace):
    line1.set_ydata(trace)
    line2.set_ydata(10**(np.array(trace)/10)*1E9)
    #spec_data[0,:] = trace
    plt.draw()
    plt.pause(0.001)

###############################################################################
# Set plots 
###############################################################################
figure1 = plt.figure(num= None, figsize=plot_size, dpi=80, facecolor='w', edgecolor='w')

ax1 = figure1.add_subplot(211)
line1, = ax1.plot(freq_MHz,np.zeros(freq_points), 'r-')

ax1.set_xlabel(xAxis_Label1)  
ax1.set_ylabel(yAxis_Label1)
ax1.xaxis.limit_range_for_scale(freq_start, freq_stop)
#ax1.yaxis.limit_range_for_scale(ymin1, ymax1)
ax1.set_xticks(np.linspace(freq_start,freq_stop,11))
ax1.set_yticks(np.linspace(ymin1,ymax1,11))
ax1.grid(which='major',axis='both')

#ax2 = figure1.add_subplot(222)
#line2, = ax2.plot(freq_MHz,np.zeros(freq_points), 'r-')
#
#ax2.set_xlabel(xAxis_Label2)  
#ax2.set_ylabel(yAxis_Label2)
#ax2.xaxis.limit_range_for_scale(freq_start, freq_stop)
#ax2.yaxis.limit_range_for_scale(ymin2, ymax2)
#ax2.set_xticks(np.linspace(freq_start,freq_stop,6))
#ax2.set_yticks(np.linspace(ymin2,ymax2,11))
#ax2.grid(which='major',axis='both')




#spec_data = np.zeros(( N_spect_plot, freq_points))
#plt.subplot(223)
#plt.imshow(spec_data )
#plt.set_data


#ax3 = figure1.add_subplot(223)
#line3, = ax3.plot(freq_MHz,np.zeros(freq_points), 'r-')
#
#ax3.set_xlabel(xAxis_Label2)  
#ax3.set_ylabel(yAxis_Label2)
#ax3.xaxis.limit_range_for_scale(freq_start, freq_stop)
#ax3.yaxis.limit_range_for_scale(ymin2, ymax2)
#ax3.set_xticks(np.linspace(freq_start,freq_stop,11))
#ax3.set_yticks(np.linspace(ymin2,ymax2,11))
#ax3.grid(which='major',axis='both')


 

plt.show(block = False)
###############################################################################
# Initialize Saving
###############################################################################
datafile=open(folder + datafile ,'w')
# Save Freq Data

for i in range(len(freq_MHz)):
    datafile.write('%f \n'%(freq_MHz[i]))

###############################################################################
# Save Data to File
###############################################################################
def Save_Data(trace,date_time_string):
    datafile.write('%s \n'%date_time_string)
    for i in range(len(trace)):
        datafile.write('%f \n'%(trace[i]))
    
###############################################################################
# Interrupt handler 
###############################################################################
class GracefulInterruptHandler(object):

    def __init__(self, sig=signal.SIGINT):
        self.sig = sig

    def __enter__(self):

        self.interrupted = False
        self.released = False

        self.original_handler = signal.getsignal(self.sig)

        def handler(signum, frame):
            self.release()
            self.interrupted = True

        signal.signal(self.sig, handler)

        return self

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):

        if self.released:
            return False

        signal.signal(self.sig, self.original_handler)

        self.released = True
###############################################################################
# Terminate Measurement 
###############################################################################        
def terminate():
    return
    

###############################################################################
# Measurement Loop
###############################################################################

with GracefulInterruptHandler() as h:
    # Start infinite Loop
    while True:
        trace,date_time_string  = Acquire_Data()
        Plot_Data(trace)
        Save_Data(trace,date_time_string)
        time.sleep(delay)
        if h.interrupted:
            print " Interrupted ... Exiting gracefully"
            terminate()
            break # Break the loop 
        

