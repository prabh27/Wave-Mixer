import wave
import struct

wavefile = wave.open('ILLBBACK.WAV','r')

length = wavefile.getnframes()
for i in range(0,length):
    wavedata = wavefile.readframes(1)
    data = struct.unpack("=h",wavedata)
    print int(data[0])
