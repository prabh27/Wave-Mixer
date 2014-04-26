import wave
import struct
import tkFileDialog
from Tkinter import *
import sys
import pyaudio
import signal
import os
final=[]
class AudioFile:
	chunk = 1024
	def __init__(self):
		self.playflag=0
		self.pauseflag=0
		self.pid=0

	def play(self,fileit):
		if self.pauseflag==1:
			self.pauseflag=0
			self.playflag=1
			os.kill(self.pid,signal.SIGCONT)
		else:

			self.pid=os.fork()
			if self.pid==0:
				self.playflag=1
				self.pauseflag=0
				""" Init audio stream """
				self.wf = wave.open(fileit, 'rb')
       	     	        	self.p = pyaudio.PyAudio()
       		 		self.stream = self.p.open(
                		format = self.p.get_format_from_width(self.wf.getsampwidth()),
                		channels = self.wf.getnchannels(),
                		rate = self.wf.getframerate(),
               	        	output = True)

        			""" Play entire file """
       	      	        	data = self.wf.readframes(self.chunk)
       		 		while data != '':
	        	   		self.stream.write(data)
                           		data = self.wf.readframes(self.chunk)

       	          		""" Graceful shutdown """
             	        	self.stream.close()
    	       			self.p.terminate()
	     	        	exit(0)

	def pause(self):
			self.playflag=0
			self.pauseflag=1
			os.kill(self.pid,signal.SIGSTOP)


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
def playit():
	a.play("rec.wav")
class Application:
    def file_input(self):
		## Input music file and its attributes
		self.files=tkFileDialog.askopenfilename()
		self.name['text']=self.files
		#print self.files
		self.fi = wave.open(self.files, 'rb')
		self.data=[]
		self.width=self.fi.getsampwidth()
		self.fmts=(None, "=B", "=h", None, "=l")
		self.fmt=self.fmts[self.width]
		self.dcs=(None, 128, 0, None, 0)
		self.dc=self.dcs[self.width]
		for i in range(self.fi.getnframes()):
			self.iframe=self.fi.readframes(1)
			(self.data).append(struct.unpack(self.fmt, self.iframe)[0])
    def ascale(self):
	if self.vara.get()!=0.0:
		for i in range(self.fi.getnframes()):
			if (self.data[i])*(self.vara.get())<SHRT_MIN:
				self.data[i]=SHRT_MIN
			elif (self.data[i])*(self.vara.get())>SHRT_MAX:
				self.data[i]=SHRT_MAX
			else:
				self.data[i]=(self.data[i])*(self.vara.get())
    def treverse(self):
	datac=[]
    	for i in range(self.fi.getnframes()):
		datac.append(self.data[i])
	j=0
	for i in range(self.fi.getnframes()-1,0,-1):
		self.data[j]=datac[i]
		j+=1

    def tscale(self):
	k=0.0
	self.dataf=[]
	if self.varc.get()==0.0:
		self.c=1
	else:
		self.c=self.varc.get()
	var=k*self.c
	while var<self.fi.getnframes():
		if var.is_integer():
			self.iframe=self.data[int(var)]
		else:
			self.iframe=0
		k+=1
		var=k*self.c
		self.dataf.append(self.iframe)
		self.iframe-=self.dc
		self.oframe=self.iframe/2;
		self.oframe+=self.dc
		self.oframe=struct.pack(self.fmt, self.oframe)
		self.fo.writeframes(self.oframe)
    def tshift(self):
	datac=[]
    	for i in range(self.fi.getnframes()):
		datac.append(self.data[i])
	inp=self.varb.get()
	if self.varb.get()>=0:
		inp=inp*self.fi.getframerate()
		for i in range(int(inp)):
			self.iframe=0
			self.data[i]=self.iframe
		j=0
		for i in range(int(inp),self.fi.getnframes()):
			self.data[i]=datac[j]
			j+=1
	else:
	  	inp=-inp*self.fi.getframerate()
		j=0
		for i in range(int(inp),self.fi.getnframes()):
			self.data[j]=datac[i]
			j+=1
		for i in range(int(inp)):
			self.iframe=0
			self.data[j]=self.iframe
			j+=1

    def play(self):
	if self.flag==0:
		self.fo = wave.open("output1.wav","w")
		self.fo.setparams(wave1.fi.getparams())
	elif self.flag==1:
		self.fo = wave.open("output2.wav","w")
		self.fo.setparams(wave2.fi.getparams())
	else:
		self.fo = wave.open("output3.wav","w")
		self.fo.setparams(wave3.fi.getparams())
	self.ascale()
	self.tshift()
	if self.checkvar1.get()==1:
		self.treverse()
	self.tscale()
	if self.flag==0:
		a.play("output1.wav")
	elif self.flag==1:
		a.play("output2.wav")
	else:
		a.play("output2.wav")
	self.fi.close()
	self.fo.close()
    def play2(self):
	if self.flag==0:
		self.fo = wave.open("output1.wav","w")
		self.fo.setparams(wave1.fi.getparams())
	elif self.flag==1:
		self.fo = wave.open("output2.wav","w")
		self.fo.setparams(wave2.fi.getparams())
	else:
		self.fo = wave.open("output3.wav","w")
		self.fo.setparams(wave3.fi.getparams())
	self.ascale()
	self.tshift()
	if self.checkvar1.get()==1:
		self.treverse()
	self.tscale()
	self.fi.close()
	self.fo.close()
    def read():
	self.fi = wave.open(self.files, 'rb')
	self.datam=[]
	self.width=self.fi.getsampwidth()
	self.fmts=(None, "=B", "=h", None, "=l")
	self.fmt=self.fmts[self.width]
	self.dcs=(None, 128, 0, None, 0)
	self.dc=self.dcs[self.width]
	for i in range(self.fi.getnframes()):
		self.iframe=self.fi.readframes(1)
		(self.data).append(struct.unpack(self.fmt, self.iframe)[0])

    def __init__(self, master,fl):
	self.flag=fl
	#Frame.__init__(self, master)
	if fl==0:
      		frame=LabelFrame(master,text="Wave1")
      		frame.place(width=300,relx=0.05,rely=0.13,anchor=NW)
	elif fl==1:
		frame=LabelFrame(master,text="Wave2")
      		frame.place(width=300,relx=0.39,rely=0.13,anchor=NW)
	else:
		frame=LabelFrame(master,text="Wave3")
      		frame.place(width=300,relx=0.72,rely=0.13,anchor=NW)

	#Select File Button
	self.button = Button(frame, text="Select File", fg="red",command=self.file_input)
	self.button.pack(side=TOP)
	#Pause Button
	self.pause = Button(frame, text="Pause", command=a.pause)
	self.pause.pack(side=BOTTOM)

	self.name=Label(frame,text='',)
	self.name.pack(side=TOP)



	#Amplitude Scale
	self.vara=DoubleVar()
	self.scale1=Scale(frame,label="Amplitude",variable=self.vara,orient=HORIZONTAL,from_=0.0,to=5.0,resolution=0.1)
	self.scale1.pack(side=TOP)

	#Play Button
	self.plays = Button(frame, text="Play", command=self.play)
	self.plays.pack(side=BOTTOM)
	#timeshift Scale
	self.varb=DoubleVar()
	self.scale2=Scale(frame,label="Time Shift",variable=self.varb,orient=HORIZONTAL,from_=-1.0,to=1.0,resolution=0.01)
	self.scale2.pack(side=TOP)

	#timescale Scale
	self.varc=DoubleVar()
	self.scale3=Scale(frame,label="Time Scaling",variable=self.varc,orient=HORIZONTAL,from_=0.0,to=8.0,resolution=0.25)
	self.scale3.pack(side=TOP)

	#Time Reversal
	self.checkvar1=IntVar()
	self.c1=Checkbutton(frame,text="Time Reversal",variable=self.checkvar1,onvalue=1,offvalue=0,height=3,width=20)
	self.c1.pack(side=TOP)

	#Modulation
	self.checkvar2=IntVar()
	self.c2=Checkbutton(frame,text="Select for Modulation",variable=self.checkvar2,onvalue=1,offvalue=0,height=3,width=20)
	self.c2.pack(side=TOP)

	#Mixing
	self.checkvar3=IntVar()
	self.c3=Checkbutton(frame,text="Select for Mixing",variable=self.checkvar3,onvalue=1,offvalue=0,height=3,width=20)
	self.c3.pack(side=TOP)

SHRT_MIN=-32767 - 1
SHRT_MAX=32767
root=Tk()
root.geometry("1200x600+500+350")
w=Label(root,text="Wave Mixer",width=10,height=3,font=35)
w.pack()
f=Frame(root,height=1,width=600,bg="black")
f.pack()
a=AudioFile()

wave1=Application(root,0)
wave2=Application(root,1)
wave3=Application(root,2)
def mixing():
	wave1.play2()
	wave2.play2()
	wave3.play2()
	fo = wave.open("output4.wav","w")
	fo.setparams(wave1.fi.getparams())
	width1=wave1.fi.getsampwidth()
	width2=wave2.fi.getsampwidth()
	width3=wave3.fi.getsampwidth()
	width=max(width1,width2,width3)
	fmts=(None, "=B", "=h", None, "=l")
	fmt=fmts[width]
	dcs=(None, 128, 0, None, 0)
	dc=dcs[width]
	for i in range(max(wave1.fi.getnframes(),wave2.fi.getnframes(),wave3.fi.getnframes())):
		final.append(0)
	for i in range(max(wave1.fi.getnframes(),wave2.fi.getnframes(),wave3.fi.getnframes())):
		final[i]=0
	for i in range(max(wave1.fi.getnframes(),wave2.fi.getnframes(),wave3.fi.getnframes())):
		if i<len(wave1.dataf) and wave1.checkvar3.get()==1:
			final[i]+=wave1.dataf[i]
		if i<len(wave2.dataf) and wave2.checkvar3.get()==1:
			final[i]+=wave2.dataf[i]
		if i<len(wave3.dataf) and wave3.checkvar3.get()==1:
			final[i]+=wave3.dataf[i]
		if final[i]<SHRT_MIN:
			final[i]=SHRT_MIN
		elif final[i]>SHRT_MAX:
			final[i]=SHRT_MAX
	for i in range(max(wave1.fi.getnframes(),wave2.fi.getnframes(),wave3.fi.getnframes())):
		iframe=final[i]
		iframe-=dc
		oframe=iframe/2;
		oframe+=dc
		oframe=struct.pack(fmt, oframe)
		fo.writeframes(oframe)
	a.play("output4.wav")
	fo.close()
def modulation():
	wave1.play2()
	wave2.play2()
	wave3.play2()
	fo = wave.open("output4.wav","w")
	fo.setparams(wave1.fi.getparams())
	width1=wave1.fi.getsampwidth()
	width2=wave2.fi.getsampwidth()
	width3=wave3.fi.getsampwidth()
	width=max(width1,width2,width3)
	fmts=(None, "=B", "=h", None, "=l")
	fmt=fmts[width]
	dcs=(None, 128, 0, None, 0)
	dc=dcs[width]
	for i in range(max(wave1.fi.getnframes(),wave2.fi.getnframes(),wave3.fi.getnframes())):
		final.append(1)
	for i in range(max(wave1.fi.getnframes(),wave2.fi.getnframes(),wave3.fi.getnframes())):
		final[i]=1
	for i in range(max(wave1.fi.getnframes(),wave2.fi.getnframes(),wave3.fi.getnframes())):
		if i<len(wave1.dataf) and wave1.checkvar2.get()==1:
			final[i]*=wave1.dataf[i]
		if i<len(wave2.dataf) and wave2.checkvar2.get()==1:
			final[i]*=wave2.dataf[i]
		if i<len(wave3.dataf) and wave3.checkvar2.get()==1:
			final[i]*=wave3.dataf[i]
		if final[i]<SHRT_MIN:
			final[i]=SHRT_MIN
		elif final[i]>SHRT_MAX:
			final[i]=SHRT_MAX
	for i in range(max(wave1.fi.getnframes(),wave2.fi.getnframes(),wave3.fi.getnframes())):
		iframe=final[i]
		iframe-=dc
		oframe=iframe/2;
		oframe+=dc
		oframe=struct.pack(fmt, oframe)
		fo.writeframes(oframe)
	a.play("output4.wav")
	fo.close()

playmix = Button(root, text="Play and Mix", command=mixing)
playmix.place(relx=0.175,rely=0.92,anchor=CENTER)
playmodulate = Button(root, text="Play and Modulate", command=modulation)
playmodulate.place(relx=0.515,rely=0.92,anchor=CENTER)
record = Button(root, text="Record", command=record)
record.place(relx=0.805,rely=0.92,anchor=CENTER)
playrecord = Button(root, text="Play Recording", command=playit)
playrecord.place(relx=0.895,rely=0.92,anchor=CENTER)
root.mainloop()

