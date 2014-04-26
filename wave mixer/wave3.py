import wave
import struct

def everyOther(v,offset=0):
    return[v[i] for i in range(offset,len(v),2)]

integer_data = []
amplitudescalingtuple=[]
fmt=[]
b=[]

def pcm_channels(wavefile):
    stream = wave.open(wavefile,'r')
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
        fmt = "%iH" % total_samples
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats")

    integer_data = struct.unpack(fmt, raw_data)
    print type(integer_data)
    del raw_data
    for i in range(0,len(integer_data)):
        if(integer_data[i]*3<=32767 and integer_data>=-32768):
            b.append(integer_data[i]*3)
        elif(integer_data[i]*3>32767):
            b.append(32767)
        elif(integer_data[i]*3<-32768):
            b.append(-32768)
    output(sample_rate,num_frames,sample_width,num_channels,fmt,b)
    print type(fmt)
def output(sample_rate,num_frames,sample_width,num_channels,fmt,array):
    r_data1=struct.pack(fmt,*(array))
    f=wave.open("112.wav",'w')
    f.setframerate(sample_rate)
    f.setnframes(num_frames)
    f.setsampwidth(sample_width)
    f.setnchannels(num_channels)
    f.writeframes(r_data1)
    f.close()

def amplitudescaling(fin,a):
    pcm_channels(fin)
    for i in range(0,len(integer_data)):
        amplitudescalingtuple[i]=integer_data[i]*a
    print amplitudescalingtuple
    output(amplitudescalingtuple)

if __name__ == "__main__":
    pcm_channels("beep.wav")
#amplitudescailing('beep.wav',2,'new.wav')

