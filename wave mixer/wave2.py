import wave
import struct

ifile = wave.open("ILLBBACK.WAV")
ofile = wave.open("1.WAV","w")

sampwidth = ifile.getsampwidth()
fmts = (None,"=B","=h",None,"=l")
fmt=fmts[sampwidth]
dcs=(None,128,0,None,0)
dc=dcs[sampwidth]

for i in range(ifile.getnframes()):
    iframe = ifile.readframes(1)

    iframe = struct.unpack(fmt,iframe)[0]
    iframe -= dc
    oframe = iframe/2
    oframe += dc
    oframe = struct.pack(fmt,oframe)
    ofile.writeframes(oframe)

ifile.close()
ofile.close()
