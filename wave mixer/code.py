import struct
import wave
import math
import sys


SHRT_MIN=-32768
SHRT_MAX=32767

print "enter file"

s=raw_input()

f=wave.open(s,'rb')


sample_width=f.getsampwidth()
frame_rate=f.getframerate()
num_channels=f.getnchannels()
num_frames=f.getnframes()

raw_data=f.readframes(num_frames)

f.close()

total_samples=num_frames * num_channels

if sample_width == 1: 
	fmt = "%iB" % total_samples
elif sample_width == 2:
        fmt = "%ih" % total_samples

integer_data=list(struct.unpack(fmt,raw_data))


integer_data2=list(integer_data)

l=len(integer_data2)

total_frames=0


print "enter factor for modulation"
choice2=input()

print "reverse or not"
reverse=input()

print "time shifted"
choice3=input()

print "factor for scaling"
choice4=input()


if choice2!=1:
########################################################### amplitude modulation
	for i in xrange(l):
		integer_data2[i]=min(max(SHRT_MIN,integer_data2[i]*choice2),SHRT_MAX)
###########################################################



if reverse==1:
########################################################### reverse
	integer_data3=integer_data2[::-1]
	if num_channels==2:
		for i in xrange(0,l,2):
			integer_data3[i],integer_data3[i+1]=integer_data3[i+1],integer_data3[i]		
############################################################
else:
	integer_data3=integer_data2



if choice3!=0:
#############################################################  time shift
	total_frames=int(abs(choice3)*frame_rate*num_channels)
	integer_data4=[]
	x=choice3/abs(choice3)*total_frames
	for i in xrange(max(0,x)):
		integer_data4.append(0)
	for i in xrange(max(0,-1*x),l):
		integer_data4.append(integer_data3[i])
	num_frames=len(integer_data4)/num_channels
	total_samples=len(integer_data4)
	l=len(integer_data4)
#############################################################
else:
	integer_data4=integer_data3



if choice4!=1:
##############################################################  time scaling
	integer_data5=[]
	z,y=0,0
	if num_channels==1:
		while(z<l):
			integer_data5.append(integer_data4[z])
			y+=choice4
			z=int(y)
	if num_channels==2:
		list1,list2=[],[]
		for i in xrange(l):
			if i%2==0:
				list1.append(integer_data4[i])
			else:
				list2.append(integer_data4[i])
		list3=[]
		list4=[]
		z,y=0,0
		while(z<l/2):
			list3.append(list1[z])
			y+=choice4
			z=int(y)
		z,y=0,0
		while(z<l/2):
			list4.append(list2[z])
			y+=choice4
			z=int(y)
		x=max(len(list3),len(list4))
		l3=len(list3)
		l4=len(list4)
		for i in xrange(x):
			integer_data5.append(list3[i])
			integer_data5.append(list4[i])
	num_frames=len(integer_data5)/num_channels
	total_samples=len(integer_data5)
##############################################################
else:
	integer_data5=integer_data4

if sample_width == 1: 
	fmt = "%iB" % (total_samples)
elif sample_width == 2:
        fmt = "%ih" % (total_samples)

raw_data2=struct.pack(fmt,*(integer_data5))

f=wave.open('new.wav','w')

f.setsampwidth(sample_width)

f.setframerate(frame_rate)

f.setnchannels(num_channels)

f.setnframes(num_frames)

f.writeframesraw(raw_data2)

f.close()
