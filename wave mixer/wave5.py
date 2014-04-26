import wave
import struct

def everyOther (v, offset=0):
    return [v[i] for i in range(offset, len(v), 2)]

def wavLoad (fname):
    wav = wave.open (fname, "r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams ()
    frames = wav.readframes (nframes * nchannels)
    out = struct.unpack_from ("%dh" % nframes * nchannels, frames)

    # Convert 2 channles to numpy arrays
    if nchannels == 2:
        left = array (list (everyOther (out, 0)))
        right = array (list  (everyOther (out, 1)))
    else:
        left = array (out)
        right = left
    print out

if __name__=="__main__":
    a=wavLoad("ILLBBACK.WAV")

