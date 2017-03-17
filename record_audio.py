from sys import byteorder
from array import array
from struct import pack
import IPython.display as ipd
import numpy as np
from scipy.fftpack import fft

import pyaudio
import wave

THRESHOLD = 500
CHUNK_SIZE = 176400
FORMAT = pyaudio.paInt16
RATE = 44100


def record():
    """
    Record a word or words from the microphone and
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the
    start and end, and pads with 0.5 seconds of
    blank sound to make sure VLC et al can play
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
                    input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)
        break
    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()
    r = np.frombuffer(r, dtype=np.int16)
    return sample_width, r


def record_to_file(path):
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h' * len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


fs, x = record()
print(x)
print(abs(fft(x)))
# print(fs)

# print("please speak a word into the microphone")
ipd.Audio(x, rate=RATE)
# print("done - result written to demo.wav")
