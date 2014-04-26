import wave
import struct

frames = []

def build(fin):
    stream = wave.open(fin,'r')
    for x in range(stream.getnframes()):
        frames.append(struct.unpack('B',stream.readframes(1)))
    return frames

def store(fout,fin):
    stream = wave.open(fin,'r')
    out = wave.open(fout,'w')
    nchannels = stream.getnchannels()
    sampwidth = stream.getsampwidth()
    framerate = stream.getframerate()
    nframes = len(frames)
    comptype = "NONE"
    compname = "not compressed"

    out.setparams((nchannels,sampwidth,framerate,nframes,comptype,compname))

    if nchannels == 1:
        for f in frames:
            data = struct.pack('B',f[0])
            out.writeframes(data)
    elif nchannels == 2:
        for f in frames:
            data = struct.pack('BB',f[0],f[1])
            out.writeframes(data)
    out.close()

def amplitudescaling(fin,fout,a):
    stream = wave.open(fin,'r')
    out = wave.open(fout,'w')
    nchannels = stream.getnchannels()
    sampwidth = stream.getsampwidth()
    framerate = stream.getframerate()
    nframes = len(frames)
    comptype = "NONE"
    compname = "not compressed"

    out.setparams((nchannels,sampwidth,framerate,nframes,comptype,compname))
    for f in range(0,len(frames)):
        frames[f]=tuple([a*x for x in frames[f]])

    if nchannels == 1:
        for f in frames:
            data = struct.pack('B',f[0])
            out.writeframes(data)
    elif nchannels == 2:
        for f in frames:
            data = struct.pack('BB',f[0],f[1])
            out.writeframes(data)
    out.close()


if __name__=="__main__":
    a=build("mono.wav")
    c = amplitudescaling("mono.wav","we.wav",0.50)

