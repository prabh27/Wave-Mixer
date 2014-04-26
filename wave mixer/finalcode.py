#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Tkinter import *
import tkMessageBox
import tkFileDialog
import wave
import struct
import tkSnack
import pyaudio
import os
import signal

pid1=0
pid2=0
pid3=0
pid4=0
pid5=0
global pauseflag1
pauseflag1=0
global pauseflag2
pauseflag2=0
global pauseflag3
pauseflag3=0

def open1():
    global wavefile1
    wavefile1 = tkFileDialog.askopenfilename()
    a=wavefile1.split('/')
#    label=Label(text='').place(x=120,y=80)
    label=Label(text=a[-1]).place(x=120,y=80)

def open2():
    global wavefile2
    wavefile2 = tkFileDialog.askopenfilename()
    a=wavefile2.split('/')
    label=Label(text=a[-1]).place(x=420,y=80)

def open3():
    global wavefile3
    wavefile3 = tkFileDialog.askopenfilename()
    a=wavefile3.split('/')
    label=Label(text=a[-1]).place(x=720,y=80)


'''class Wave():

    def __init__(self):
        self.stream = None
        self.num_channels = None
        self.sample_rate = None
        self.sample_width = None
        self.num_frames = None
        self.total_samples = None
        self.fmt = None
        self.integer_data = None
    def Open(self,wavefile):
        self.stream = wave.open(wavefile,'r')
        self.num_channels = self.stream.getnchannels()
        self.sample_rate = self.stream.getframerate()
        self.sample_width = self.stream.getsampwidth()
        self.num_frames = self.stream.getnframes()
        self.raw_data = self.stream.readframes(self.num_frames)
        self.stream.close()
        self.total_samples = self.num_frames * self.num_channels
        if self.sample_width == 1:
            self.fmt = "%iB" % self.total_samples
        elif self.sample_width == 2:
            self.fmt = "%ih" % self.total_samples
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats")
        self.integer_data = struct.unpack(self.fmt, self.raw_data)
'''


def Playwavfile1():
    global pauseflag1
    global wavefile1
    stream = wave.open(wavefile1,'rb')
    num_channels = stream.getnchannels()
    sample_rate = stream.getframerate()
    sample_width = stream.getsampwidth()
    num_frames = stream.getnframes()
    raw_data = stream.readframes(num_frames)
    stream.close()
    total_samples = num_frames * num_channels

    if sample_width == 1:
        fmt = "%ib" % total_samples
    elif sample_width == 2:
        fmt = "%ih" % total_samples
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats")

    integer_data = struct.unpack(fmt, raw_data)
    del raw_data
    amplitudescalar1=amp1.get()
    if(amplitudescalar1!=0):
        amplitudescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave1.wav",amplitudescalar1)
    if(amplitudescalar1==0):
        amplitudescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave1.wav",1)
    if(timeshift1.get()!=0):
        timeshifting(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave1.wav",timeshift1.get())
    if(timescal1.get()!=0):
        Timescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave1.wav",timescal1.get())
    if(timerev1.get()==1):
        timereversal(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave1.wav")
    fplay = wave.open("newwave1.wav",'rb')
    global pid1
    if(pauseflag1==1):
        os.kill(pid1,signal.SIGCONT)
        pauseflag1=0
    else:
        pid1 = os.fork()
        if pid1==0:
            p = pyaudio.PyAudio()
            play = p.open(format = p.get_format_from_width(fplay.getsampwidth()),channels = fplay.getnchannels(),rate = fplay.getframerate(), output = True)
            readdata = fplay.readframes(1024)
            while readdata != '':
                play.write(readdata)
                readdata = fplay.readframes(1024)
            play.stop_stream()
            play.close()
            p.terminate()
            sys.exit(0)

def Pausewavfile1():
    os.kill(pid1,signal.SIGSTOP)
    global pauseflag1
    pauseflag1=1

def Pausewavfile2():
    os.kill(pid2,signal.SIGSTOP)
    global pauseflag2
    pauseflag2=1

def Pausewavfile3():
    os.kill(pid3,signal.SIGSTOP)
    global pauseflag3
    pauseflag3=1


def Playwavfile2():
    global wavefile2
    global pauseflag2
    stream = wave.open(wavefile2,'r')
    num_channels = stream.getnchannels()
    sample_rate = stream.getframerate()
    sample_width = stream.getsampwidth()
    num_frames = stream.getnframes()
    raw_data = stream.readframes(num_frames)
    stream.close()
    total_samples = num_frames * num_channels

    if sample_width == 1:
        fmt = "%ib" % total_samples
    elif sample_width == 2:
        fmt = "%ih" % total_samples
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats")

    integer_data = struct.unpack(fmt, raw_data)
    del raw_data
    amplitudescalar2=amp2.get()
    if(amplitudescalar2!=0):
        amplitudescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave2.wav",amplitudescalar2)
    if(amplitudescalar2==0):
        amplitudescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave2.wav",1)
 #   print timerev1.get()
    if(timeshift2.get()!=0):
        timeshifting(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave2.wav",timeshift2.get())
    if(timescal2.get()!=0):
        Timescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave2.wav",timescal2.get())
    if(timerev2.get()==1):
        timereversal(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave2.wav")
    fplay = wave.open("newwave2.wav",'rb')
    global pid2
    if(pauseflag2==1):
        os.kill(pid2,signal.SIGCONT)
        pauseflag2=0
    else:
        pid2 = os.fork()
        if pid2==0:
            p = pyaudio.PyAudio()
            play = p.open(format = p.get_format_from_width(fplay.getsampwidth()),channels = fplay.getnchannels(),rate = fplay.getframerate(), output = True)
            readdata = fplay.readframes(1024)
            while readdata != '':
                play.write(readdata)
                readdata = fplay.readframes(1024)
            play.close()
            p.terminate()
            sys.exit(0)


def Playwavfile3():
    global wavefile3
    global pauseflag3
    stream = wave.open(wavefile3,'r')
    num_channels = stream.getnchannels()
    sample_rate = stream.getframerate()
    sample_width = stream.getsampwidth()
    num_frames = stream.getnframes()
    raw_data = stream.readframes(num_frames)
    stream.close()
    total_samples = num_frames * num_channels

    if sample_width == 1:
        fmt = "%ib" % total_samples
    elif sample_width == 2:
        fmt = "%ih" % total_samples
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats")

    integer_data = struct.unpack(fmt, raw_data)
    del raw_data
    amplitudescalar3=amp3.get()
    if(amplitudescalar3!=0):
        amplitudescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave3.wav",amplitudescalar3)
    if(amplitudescalar3==0):
        amplitudescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave3.wav",1)
    print timerev3.get()
    if(timeshift3.get()!=0):
        timeshifting(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave3.wav",timeshift3.get())
    if(timescal3.get()!=0):
        Timescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave3.wav",timescal3.get())
    if(timerev3.get()==1):
        timereversal(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,"newwave3.wav")
   # chunk = 1024

    CHUNK=1024
    wtf=wave.open("newwave3.wav",'rb')
    global pid3
    if(pauseflag3==1):
        os.kill(pid3,signal.SIGCONT)
        pauseflag3=0
    else:
        pid3 = os.fork()
        if pid3==0:
            p=pyaudio.PyAudio()
            stream=p.open(format=p.get_format_from_width(wtf.getsampwidth()),channels=wtf.getnchannels(),rate=wtf.getframerate(),output=True)
            data = wtf.readframes(CHUNK)
            while data != '':
                stream.write(data)
                data = wtf.readframes(CHUNK)
            stream.stop_stream()
            stream.close()
            p.terminate()
            sys.exit(0)
  #  fplay = wave.open("newwave3.wav",'rb')
 #   p = pyaudio.PyAudio()
#    play = p.open(format = p.get_format_from_width(fplay.getsampwidth()),channels = fplay.getnchannels(),rate = fplay.getframerate(), output = True)
 #   readdata = fplay.readframes(chunk)
  #  while readdata != '':
   #     play.write(readdata)
    #    readdata = fplay.readframes(chunk)
#    play.stop_stream()
 #   play.close()
  #  p.terminate()






def output(fmt,sample_rate,num_frames,sample_width,num_channels,fout,array):
    if sample_width == 1:
        fmt = "%ib" % len(array)
    elif sample_width == 2:
        fmt = "%ih" % len(array)
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats")
    q_data=struct.pack(fmt,*((array)))
    q=wave.open(fout,'w')
    q.setframerate(sample_rate)
    q.setnframes(num_frames)
    q.setsampwidth(sample_width)
    q.setnchannels(num_channels)
    q.writeframes(q_data)
    q.close()
def amplitudescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,fout,amplitudescalar):
    amplitudescalingtuple=[]
    for i in range(0,len(integer_data)):
        #print type(amplitudescalar)
        if(integer_data[i]*amplitudescalar<=32767 and integer_data[i]*amplitudescalar>=-32768):
            amplitudescalingtuple.append(integer_data[i]*amplitudescalar)
        elif(integer_data[i]*amplitudescalar>32767):
            amplitudescalingtuple.append(32767)
        elif(integer_data[i]*amplitudescalar<-32768):
            amplitudescalingtuple.append(-32768)
    output(fmt,sample_rate,num_frames,sample_width,num_channels,fout,amplitudescalingtuple)

def timereversal(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,fout):
    timereversaltuple=[]
    for i in range(len(integer_data)-1,0,-1):
        timereversaltuple.append(integer_data[i])
    output(fmt,sample_rate,len(timereversaltuple),sample_width,num_channels,fout,timereversaltuple)

def timeshifting(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,fout,timeshifter):
    timeshiftertuple=[]
    if(timeshifter>0):
        if(num_channels==1):
            print timeshifter*num_frames
            print len(integer_data)
            for i in range(0,1*timeshifter*num_frames):
                timeshiftertuple.append(0)
            for i in range(0,len(integer_data)):
                timeshiftertuple.append(integer_data[i])
            output(fmt,sample_rate,len(timeshiftertuple),sample_width,num_channels,fout,timeshiftertuple)
        if(num_channels==2):
            for i in range(0,2*timeshifter*num_frames):
                timeshiftertuple.append(0)
            for i in range(0,len(integer_data)):
                timeshiftertuple.append(integer_data[i])
            output(fmt,sample_rate,len(timeshiftertuple)/2,sample_width,num_channels,fout,timeshiftertuple)
    if(timeshifter<0):
        if(num_channels==1):
            for i in range(1*timeshifter*num_frames,len(integer_data)):
                timeshiftertuple.append(integer_data[i])
            output(fmt,sample_rate,len(timeshiftertuple),sample_width,num_channels,fout,timeshiftertuple)
        if(num_channels==2):
            for i in range(2*timeshifter*num_frames,len(integer_data)):
                timeshiftertuple.append(integer_data[i])
            output(fmt,sample_rate,len(timeshiftertuple)/2,sample_width,num_channels,fout,timeshiftertuple)


def Timescaling(fmt,sample_rate,num_frames,sample_width,num_channels,integer_data,fout,timescaler):
    timescalertuple=[]
    odd=[]
    even=[]
    neweven=[]
    newodd=[]
    for i in range(0,len(integer_data),2):
        even.append(integer_data[i])
    for i in range(1,len(integer_data),2):
        odd.append(integer_data[i])
    i=1
    while((i*timescaler)<len(even)):
        neweven.append(even[(int(i*timescaler))])
        i=i+1
    i=1
    while((i*timescaler)<len(odd)):
        newodd.append(odd[(int(i*timescaler))])
        i=i+1
    i=0
    if(len(newodd)>len(neweven)):
        while(i<len(newodd)):
            if(i<len(neweven)):
                timescalertuple.append(neweven[i])
            else:
                timescalertuple.append(0)
            timescalertuple.append(newodd[i])
            i=i+1
    i=0
    if(len(neweven)>len(newodd)):
        while(i<len(neweven)):
            timescalertuple.append(neweven[i])
            if(i<len(newodd)):
                timescalertuple.append(newodd[i])
            else:
                timescalertuple.append(0)
            i=i+1
    output(fmt,sample_rate,len(timescalertuple),sample_width,num_channels,fout,timescalertuple)



def Playmixedfiles():
    mixingtuple=[]
    print mixingtuple
    if(mixing1.get()==1):
        stream1 = wave.open(wavefile1,'r')
        num_channels1 = stream1.getnchannels()
        sample_rate1 = stream1.getframerate()
        sample_width1 = stream1.getsampwidth()
        num_frames1 = stream1.getnframes()
        raw_data1 = stream1.readframes(num_frames1)
        stream1.close()
        total_samples1 = num_frames1 * num_channels1
        if sample_width1 == 1:
            fmt1 = "%iB" % total_samples1
        elif sample_width1 == 2:
            fmt1 = "%ih" % total_samples1
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats")
        integer_data1 = struct.unpack(fmt1, raw_data1)
        del raw_data1
    if(mixing2.get()==1):
        stream2 = wave.open(wavefile2,'r')
        num_channels2 = stream2.getnchannels()
        sample_rate2 = stream2.getframerate()
        sample_width2 = stream2.getsampwidth()
        num_frames2 = stream2.getnframes()
        raw_data2 = stream2.readframes(num_frames2)
        stream2.close()
        total_samples2 = num_frames2 * num_channels2
        if sample_width2==1:
            fmt2 = "%iB" % total_samples2
        elif sample_width2 == 2:
            fmt2 = "%ih" % total_samples2
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats")
        integer_data2 = struct.unpack(fmt2,raw_data2)
        del raw_data2
    if(mixing3.get()==1):
        stream3 = wave.open(wavefile3,'r')
        num_channels3 = stream3.getnchannels()
        sample_rate3 = stream3.getframerate()
        sample_width3 = stream3.getsampwidth()
        num_frames3 = stream3.getnframes()
        raw_data3 = stream3.readframes(num_frames3)
        stream3.close()
        total_samples3 = num_frames3 * num_channels3
        print sample_width3
        if sample_width3==1:
            fmt3 = "%iB" % total_samples3
        elif sample_width3==2:
            fmt3 = "%ih" % total_samples3
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats")
        integer_data3 = struct.unpack(fmt3,raw_data3)
        del raw_data3
    if(mixing1.get()==1 and mixing3.get()!=1):
        if (mixing2.get()==1):
            print "aayaa\n"
            if(len(integer_data1)>=len(integer_data2)):
                for i in range(0,len(integer_data2)):
                    if((integer_data1[i]+integer_data2[i])<-32768):
                        mixingtuple.append(-32768)
                    elif((integer_data1[i]+integer_data2[i])>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i])
                for i in range(len(integer_data2),len(integer_data1)):
                    mixingtuple.append(integer_data1[i])
                output(fmt1,sample_rate1,len(mixingtuple),sample_width1,num_channels1,"mixed_wave.wav",mixingtuple)
            elif (len(integer_data2)>len(integer_data1)):
                for i in range(0,len(integer_data1)):
                    if((integer_data1[i]+integer_data2[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i])
                for i in range(len(integer_data1),len(integer_data2)):
                    mixingtuple.append(integer_data2[i])
                output(fmt2,sample_rate2,len(mixingtuple),sample_width2,num_channels2,"mixed_wave.wav",mixingtuple)
        elif (mixing3.get()==1):
            if(len(integer_data1)>len(integer_data3)):
                for i in range(0,len(integer_data3)):
                    if((integer_data1[i]+integer_data3[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data3[i])
                for i in range(len(integer_data3),len(integer_data1)):
                    mixingtuple.append(integer_data1[i])
                output(fmt1,sample_rate1,len(mixingtuple),sample_width1,num_channels1,"mixed_wave.wav",mixingtuple)
            elif(len(integer_data3)>len(integer_data1)):
                for i in range(0,len(integer_data1)):
                    if((integer_data1[i]+integer_data3[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data3[i])
                for i in range(len(integer_data1),len(integer_data3)):
                    mixingtuple.append(integer_data3[i])
                output(fmt3,sample_rate3,len(mixingtuple),sample_width3,num_channels3,"mixed_wave.wav",mixingtuple)
    elif((mixing2.get()==1) and (mixing3.get()==1)):
        if(len(integer_data2)>len(integer_data3)):
            for i in range(0,len(integer_data3)):
                if((integer_data2[i]+integer_data3[i])<-32768):
                    mixingtuple.append(-32768)
                elif(integer_data2[i]+integer_data3[i]>32767):
                    mixingtuple.append(32767)
                else:
                    mixingtuple.append(integer_data2[i]+integer_data3[i])
            for i in range(len(integer_data3),len(integer_data1)):
                mixingtuple.append(integer_data1[i])
            output(fmt2,sample_rate2,len(mixingtuple),sample_width2,num_channels2,"mixed_wave.wav",mixingtuple)
        elif (len(integer_data3)>len(integer_data2)):
            for i in range(0,len(integer_data2)):
                if((integer_data2[i]+integer_data3[i])<-32768):
                    mixingtuple.append(-32768)
                elif(integer_data2[i]+integer_data3[i]>32767):
                    mixingtuple.append(32767)
                else:
                    mixingtuple.append(integer_data2[i]+integer_data3[i])
            for i in range(len(integer_data2),len(integer_data3)):
                mixingtuple.append(integer_data3[i])
            output(fmt3,sample_rate3,len(mixingtuple),sample_width3,num_channels3,"mixed_wave.wav",mixingtuple)
    elif((mixing1.get()==1) and (mixing2.get()==1) and (mixing3.get()==1)):
        if((len(integer_data1)>len(integer_data2)) and (len(integer_data1)>len(integer_data3))):
            if(len(integer_data2)>len(integer_data3)):
                for i in range(0,len(integer_data3)):
                    if(integer_data1[i]+integer_data2[i]+integer_data3[i]<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                for i in range(len(integer_data3),len(integer_data2)):
                    if((integer_data1[i]+integer_data2[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i])
                for i in range(len(integer_data2),len(integer_data1)):
                    mixingtuple.append(integer_data1[i])
                output(fmt1,sample_rate1,len(mixingtuple),sample_width1,num_channels1,"mixed_wave.wav",mixingtuple)
            elif(len(integer_data3)>len(integer_data2)):
                for i in range(0,len(integer_data2)):
                    #mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                    if(integer_data1[i]+integer_data2[i]+integer_data3[i]<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                for i in range(len(integer_data2),len(integer_data3)):
                    if((integer_data1[i]+integer_data3[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data3[i])
                for i in range(len(integer_data3),len(integer_data1)):
                    mixingtuple.append(integer_data1[i])
                output(fmt1,sample_rate1,len(mixingtuple),sample_width1,num_channels1,"mixed_wave.wav",mixingtuple)
        if((len(integer_data2)>len(integer_data1)) and (len(integer_data2)>len(integer_data3))):
            if(len(integer_data1)>len(integer_data3)):
                for i in range(0,len(integer_data3)):
                    #mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                    if(integer_data1[i]+integer_data2[i]+integer_data3[i]<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                for i in range(len(integer_data3),len(integer_data1)):
                    #mixingtuple.append(integer_data2[i]+integer_data1[i])
                    if((integer_data1[i]+integer_data2[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i])
                for i in range(len(integer_data1),len(integer_data2)):
                    mixingtuple.append(integer_data2[i])
                output(fmt2,sample_rate2,len(mixingtuple),sample_width2,num_channels2,"mixed_wave.wav",mixingtuple)
            elif(len(integer_data3)>len(integer_data1)):
                for i in range(0,len(integer_data1)):
                    #mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                    if(integer_data1[i]+integer_data2[i]+integer_data3[i]<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                for i in range(len(integer_data1),len(integer_data3)):
                    #mixingtuple.append(integer_data3[i]+integer_data2[i])
                    if((integer_data3[i]+integer_data2[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data3[i]+integer_data2[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data3[i]+integer_data2[i])
                for i in range(len(integer_data3),len(integer_data2)):
                    mixingtuple.append(integer_data2[i])
                output(fmt2,sample_rate2,len(mixingtuple),sample_width2,num_channels2,"mixed_wave.wav",mixingtuple)
        if((len(integer_data3)>len(integer_data1)) and (len(integer_data3)>len(integer_data2))):
            if(len(integer_data1)>len(integer_data2)):
                for i in range(0,len(integer_data2)):
                    #mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                    if(integer_data1[i]+integer_data2[i]+integer_data3[i]<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                for i in range(len(integer_data2),len(integer_data1)):
                    #mixingtuple.append(integer_data3[i]+integer_data1[i])
                    if((integer_data3[i]+integer_data1[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data3[i]+integer_data1[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data3[i]+integer_data1[i])
                for i in range(len(integer_data1),len(integer_data3)):
                    mixingtuple.append(integer_data3[i])
                output(fmt3,sample_rate3,len(mixingtuple),sample_width3,num_channels3,"mixed_wave.wav",mixingtuple)
            elif(len(integer_data2)>len(integer_data1)):
                for i in range(0,len(integer_data1)):
                    #mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                    if(integer_data1[i]+integer_data2[i]+integer_data3[i]<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data1[i]+integer_data2[i]+integer_data3[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data1[i]+integer_data2[i]+integer_data3[i])
                for i in range(len(integer_data1),len(integer_data2)):
                    #mixingtuple.append(integer_data1[i]+integer_data3[i])
                    if((integer_data3[i]+integer_data2[i])<-32768):
                        mixingtuple.append(-32768)
                    elif(integer_data3[i]+integer_data2[i]>32767):
                        mixingtuple.append(32767)
                    else:
                        mixingtuple.append(integer_data3[i]+integer_data2[i])
                for i in range(len(integer_data2),len(integer_data3)):
                    mixingtuple.append(integer_data3[i])
                output(fmt3,sample_rate3,len(mixingtuple),sample_width3,num_channels3,"mixed_wave.wav",mixingtuple)
    CHUNK=1024
    wtf=wave.open("mixed_wave.wav",'rb')
    global pid4
    pid4 = os.fork()
    if pid4==0:
        p=pyaudio.PyAudio()
        stream=p.open(format=p.get_format_from_width(wtf.getsampwidth()),channels=wtf.getnchannels(),rate=wtf.getframerate(),output=True)
        data = wtf.readframes(CHUNK)
        while data != '':
            stream.write(data)
            data = wtf.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()
        sys.exit(0)


def Playmodulatedfiles():
    modulatedtuple=[]
    if(modulation1.get()==1):
        stream1 = wave.open(wavefile1,'r')
        num_channels1 = stream1.getnchannels()
        sample_rate1 = stream1.getframerate()
        sample_width1 = stream1.getsampwidth()
        num_frames1 = stream1.getnframes()
        raw_data1 = stream1.readframes(num_frames1)
        stream1.close()
        total_samples1 = num_frames1 * num_channels1
        if sample_width1 == 1:
            fmt1 = "%iB" % total_samples1
        elif sample_width1 == 2:
            fmt1 = "%ih" % total_samples1
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats")
        integer_data1 = struct.unpack(fmt1, raw_data1)
        del raw_data1
    if(modulation2.get()==1):
        stream2 = wave.open(wavefile2,'r')
        num_channels2 = stream2.getnchannels()
        sample_rate2 = stream2.getframerate()
        sample_width2 = stream2.getsampwidth()
        num_frames2 = stream2.getnframes()
        raw_data2 = stream2.readframes(num_frames2)
        stream2.close()
        total_samples2 = num_frames2 * num_channels2
        if sample_width2==1:
            fmt2 = "%iB" % total_samples2
        elif sample_width2 == 2:
            fmt2 = "%ih" % total_samples2
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats")
        integer_data2 = struct.unpack(fmt2,raw_data2)
        del raw_data2
    if(modulation3.get()==1):
        stream3 = wave.open(wavefile3,'r')
        num_channels3 = stream3.getnchannels()
        sample_rate3 = stream3.getframerate()
        sample_width3 = stream3.getsampwidth()
        num_frames3 = stream3.getnframes()
        raw_data3 = stream3.readframes(num_frames3)
        stream3.close()
        total_samples3 = num_frames3 * num_channels3
        print sample_width3
        if sample_width3==1:
            fmt3 = "%iB" % total_samples3
        elif sample_width3==2:
            fmt3 = "%ih" % total_samples3
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats")
        integer_data3 = struct.unpack(fmt3,raw_data3)
        del raw_data3
    if(modulation1.get()==1 and modulation3.get()!=1):
        if(modulation2.get()==1):
            for i in range(0,min(len(integer_data1),len(integer_data2))):
                if((integer_data1[i]*integer_data2[i])>32767):
                    modulatedtuple.append(32767)
                elif((integer_data1[i]*integer_data2[i])<-32768):
                    modulatedtuple.append(-32768)
                else:
                    modulatedtuple.append(integer_data1[i]*integer_data2[i])
            output(fmt2,sample_rate2,len(modulatedtuple),sample_width2,num_channels2,"modulated_wave.wav",modulatedtuple)
        elif(modulation3.get()==1):
            for i in range(0,min(len(integer_data1),len(integer_data3))):
                if((integer_data1[i]*integer_data3[i])>32767):
                    modulatedtuple.append(32767)
                elif((integer_data1[i]*integer_data3[i])<-32768):
                    modulatedtuple.append(-32768)
                else:
                    modulatedtuple.append(integer_data1[i]*integer_data3[i])
            output(fmt3,sample_rate3,len(modulatedtuple),sample_width3,num_channels3,"modulated_wave.wav",modulatedtuple)
    if(modulation2.get()==1 and modulation3.get()==1):
        for i in range(0,min(len(integer_data3),len(integer_data2))):
            if((integer_data3[i]*integer_data2[i])>32767):
                    modulatedtuple.append(32767)
            elif((integer_data3[i]*integer_data2[i])<-32768):
                modulatedtuple.append(-32768)
            else:
                modulatedtuple.append(integer_data3[i]*integer_data2[i])
        output(fmt2,sample_rate2,len(modulatedtuple),sample_width2,num_channels2,"modulated_wave.wav",modulatedtuple)
    if(modulation1.get()==1 and modulation2.get()==1 and modulation3.get()==1):
        for i in range(0,min(len(integer_data1),len(integer_data2),len(integer_data3))):
            if((integer_data3[i]*integer_data2[i]*integer_data1[i])>32767):
                    modulatedtuple.append(32767)
            elif((integer_data3[i]*integer_data2[i]*integer_data1[i])<-32768):
                modulatedtuple.append(-32768)
            else:
                modulatedtuple.append(integer_data3[i]*integer_data2[i]*integer_data1[i])
        output(fmt2,sample_rate2,len(modulatedtuple),sample_width2,num_channels2,"modulated_wave.wav",modulatedtuple)
    CHUNK=1024
    wtf=wave.open("modulated_wave.wav",'rb')
    global pid5
    pid5 = os.fork()
    if pid5==0:
        p=pyaudio.PyAudio()
        stream=p.open(format=p.get_format_from_width(wtf.getsampwidth()),channels=wtf.getnchannels(),rate=wtf.getframerate(),output=True)
        data = wtf.readframes(CHUNK)
        while data != '':
            stream.write(data)
            data = wtf.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()
        sys.exit(0)



def record():
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    arrr=[]
    RATE = 44100
    RECORD_SECONDS = 10
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS, rate=RATE, input=True,output=True,frames_per_buffer=chunk)
    print "Recording"
    for i in range(0, 44100 / chunk * RECORD_SECONDS):
        data = stream.read(chunk)
        arrr.append(data)
    wf = wave.open("rec.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(arrr))
    wf.close()
    print "Recording Complete"
    stream.stop_stream()
    stream.close()
    p.terminate()

def playrec():
    CHUNK=1024
    wtf=wave.open("rec.wav",'rb')
    global pid6
    pid6 = os.fork()
    if pid6==0:
        p=pyaudio.PyAudio()
        stream=p.open(format=p.get_format_from_width(wtf.getsampwidth()),channels=wtf.getnchannels(),rate=wtf.getframerate(),output=True)
        data = wtf.readframes(CHUNK)
        while data != '':
            stream.write(data)
            data = wtf.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()
        sys.exit(0)







if __name__ == "__main__":
    ''' wave1 = Wave()
    wave2 = Wave()
    wave3 = Wave()'''
Gui = Tk()
Gui.geometry('900x600')
Gui.title('Wave Mixer')
amp1 = IntVar()
timescal1= IntVar()
timeshift1= IntVar()
timerev1 = IntVar()
mixing1 = IntVar()
modulation1 = IntVar()
amp2 = IntVar()
timescal2 = IntVar()
timeshift2 = IntVar()
timerev2 = IntVar()
mixing2 = IntVar()
modulation2 = IntVar()
amp3 = IntVar()
timescal3 = IntVar()
timeshift3 = IntVar()
timerev3 = IntVar()
mixing3 = IntVar()
modulation3 = IntVar()
graphics=Canvas(Gui)
graphics.pack()
#graphics.create_line(0,40,1000,40,fill='black')
graphics.create_text(180,20,font=("Purisa",20),text="Wave Mixer")
#graphics.create_line(5,50,250,50,fill="black")
#graphics.create_text(20,50,font=("Pursia",10),text="Wave 1")
label1=Label(text="Wave 1").place(x=100,y=40)
button1 = Button(text='Select File',command=open1).place(x=20,y=70)
Amplitude1 = Scale(Gui,label='Amplitude',orient=HORIZONTAL,length=220,width=20,sliderlength=10,from_=0,to=5,tickinterval=1,variable=amp1).place(x=20,y=100)
playbutton1 = Button(text='Play',fg='black',command=Playwavfile1).place(x=20,y=500)
pausebutton1 = Button(text='Pause',fg='black',command=Pausewavfile1).place(x=90,y=500)
#stopbutton1 = Button(text='Stop',fg='black').place(x=130,y=500)
timescaling1 = Scale(Gui,label='Time Scale',orient = HORIZONTAL,length = 220, width = 20,sliderlength = 10,from_=0,to=4,tickinterval=1,variable=timescal1).place(x=20, y=200)
timeshifting1 = Scale(Gui,label='Time Shift',orient=HORIZONTAL,length = 220,width=20,sliderlength=10,from_=-1,to=1,tickinterval=1,variable=timeshift1).place(x=20,y=300)
timereversal1 = Checkbutton(Gui,text='Time Reversal',variable=timerev1).place(x=20,y=400)
mix1 = Checkbutton(Gui,text = "Select for Mixing",variable=mixing1).place(x=20,y=420)
print mixing1
modul1 = Checkbutton(Gui,text = "Select for Modulation",variable=modulation1).place(x=20,y=440)

label2=Label(text="Wave 2").place(x=400,y=40)
button2 = Button(text='Select File',command=open2).place(x=320,y=70)
Amplitude2 = Scale(Gui,label='Amplitude',orient=HORIZONTAL,length=220,width=20,sliderlength=10,from_=0,to=5,tickinterval=1,variable=amp2).  place(x=320,y=100)
playbutton2 = Button(text='Play',fg='black',command=Playwavfile2).place(x=320,y=500)
pausebutton2 = Button(text='Pause',fg='black',command=Pausewavfile2).place(x=390,y=500)
timescaling2 = Scale(Gui,label='Time Scale',orient = HORIZONTAL,length = 220, width = 20,sliderlength = 10,from_=0,to=4,tickinterval=1,      variable=timescal2).place(x=320, y=200)
timeshifting2 = Scale(Gui,label='Time Shift',orient=HORIZONTAL,length = 220,width=20,sliderlength=10,from_=-1,to=1,tickinterval=1,            variable=timeshift2).place(x=320,y=300)
timereversal2 = Checkbutton(Gui,text='Time Reversal',variable=timerev2).place(x=320,y=400)
mix2 = Checkbutton(Gui,text = "Select for Mixing",variable=mixing2).place(x=320,y=420)
modul2 = Checkbutton(Gui,text = "Select for Modulation",variable=modulation2).place(x=320,y=440)

label3=Label(text="Wave 3").place(x=700,y=40)
button3 = Button(text='Select File',command=open3).place(x=620,y=70)
Amplitude3 = Scale(Gui,label='Amplitude',orient=HORIZONTAL,length=220,width=20,sliderlength=10,from_=0,to=5,tickinterval=1,variable=amp3).  place(x=620,y=100)
playbutton3 = Button(text='Play',fg='black',command=Playwavfile3).place(x=620,y=500)
pausebutton3 = Button(text="Pause",fg='black',command=Pausewavfile3).place(x=690,y=500)
timescaling3 = Scale(Gui,label='Time Scale',orient = HORIZONTAL,length = 220, width = 20,sliderlength = 10,from_=0,to=4,tickinterval=1,      variable=timescal3).place(x=620, y=200)
timeshifting3 = Scale(Gui,label='Time Shift',orient=HORIZONTAL,length = 220,width=20,sliderlength=10,from_=-1,to=1,tickinterval=1,            variable=timeshift3).place(x=620,y=300)
timereversal3 = Checkbutton(Gui,text='Time Reversal',variable=timerev3).place(x=620,y=400)
mix3 = Checkbutton(Gui,text = "Select for Mixing",variable=mixing3).place(x=620,y=420)
modul3 = Checkbutton(Gui,text = "Select for Modulation",variable=modulation3).place(x=620,y=440)


Mixing = Button(text="Mix and Play",fg='black',command=Playmixedfiles).place(x=100,y=550)
Modulation = Button(text="Modulate and Play",fg='black',command=Playmodulatedfiles).place(x=230,y=550)
Record = Button(text="Record",fg="black",command=record).place(x=400,y=550)
playrec = Button(text="Play Recording",fg="black",command=playrec).place(x=500,y=550)


'''
label2=Label(text="Wave 2").place(x=400,y=40)
button2 = Button(text='Select File',command=wave2.Open()).place(x=320,y=70)
Amplitude2 = Scale(Gui,label='Amplitude',orient=HORIZONTAL,length=220,width=20,sliderlength=10,from_=-50,to=50,tickinterval=20,command=Store_value_amplitude2).place(x=320,y=100)
playbutton2 = Button(text='►',fg='black',command=Playwavfile2).place(x=320,y=600)
timescaling2 = Scale(Gui,label='Time Scale',orient = HORIZONTAL,length = 220, width = 20,sliderlength = 10,from_=-10,to=10,tickinterval=2,command=Store_value_timescaling2).place(x=320,y=200)
timeshifting2 = Scale(Gui,label='Time Shift',orient=HORIZONTAL,length = 220,width=20,sliderlength=10,from_=-10,to=10,tickinterval=2,command=Store_value_timeshifting2).place(x=320,     y=300)
label3=Label(text="Wave 3").place(x=700,y=40)
button3 = Button(text='Select File',command=Open3).place(x=620,y=70)
Amplitude3 = Scale(Gui,label='Amplitude',orient=HORIZONTAL,length=220,width=20,sliderlength=10,from_=-50,to=50,tickinterval=20,command=Store_value_amplitude3).place(x=620,y=100)
playbutton3 = Button(text='►',fg='black',command=Playwavfile3).place(x=620,y=600)
    timescaling3 = Scale(Gui,label='Time Scale',orient = HORIZONTAL,length = 220, width = 20,sliderlength = 10,from_=-10,to=10,tickinterval=2,command=Store_value_timescaling3).place(x=620,y=200)
timeshifting3 = Scale(Gui,label='Time Shift',orient=HORIZONTAL,length = 220,width=20,sliderlength=10,from_=-10,to=10,tickinterval=2,command=Store_value_timeshifting3).place(x=620,     y=300)
'''
Gui.mainloop()

