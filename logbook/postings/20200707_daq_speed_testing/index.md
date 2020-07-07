From June 15th to July 7th, Dr. Slosar and I have been investigating the speed at which the BMX data can be processed for various different parameters using mock 
data. We have also experimented with two different kinds of mock input data: input data as real and imaginary components and input data as mplitude and phase 
components.

The up to date code for this investigation can be found in **https://github.com/bmxdemo/daqspeed** or on the bmxdaq1 server in **/home/bmx/josborn/daqspeed**. The prograam 
that handles the input data as real and imaginary components is called main.cpp and the program that handles the input daataa asa amplitude and phase components is 
called ampPhase.cpp. Both of these prograams are located in daqspeed/src, and the compilation details for these programs is written in daqspeed/MakeFile.

In this posting directory, I have attached series of images of the tables of average packet processing times vs numerous parameters that resulted from this 
investigation. The chief result is that it appeaars that it is **faster** to handle the input data as **real** and **imaginary** components than as amplitude and phase 
components. 

![realImag-FFTSIZZE](https://github.com/bmxdemo/bmxproject/blob/master/logbook/postings/20200707_daq_speed_testing/realImag-FFTSIZE.png)


Jesse Osborn - July 7th, 2020
