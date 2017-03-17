from pylab import *
from scipy.io import wavfile
from scipy.fftpack import fft
import numpy as np

sampFreq, snd = wavfile.read('Test.wav')

print(snd.dtype)
print(snd.shape)

# The duration of the wav file
duration = snd.shape[0] / sampFreq
print("Duration =", duration, "s")

# Plotting the Tone

timeArray = np.arange(0, 5292, 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  # scale to milliseconds

# plot(timeArray, snd[:, 0], color='k')
# ylabel('Amplitude')
# xlabel('Time (ms)')

# show()

# Plotting the Frequency Content
print(snd[:, 0])
n = len(snd[:, 0])
p = fft(snd[:, 0])  # take the fourier transform
print(p)
p = abs(p)
print(p)
