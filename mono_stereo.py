import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import IPython.display as ipd

filename = input("Enter the .wav file name (including extension): ")

# Load the audio file
y, sr = librosa.load(filename, sr=44100)

#new stereo array
#stereo_array = np.hstack((y,y))
stereo_array = np.array([y,y])

#convert to vertical columns of identical data
stereo_out = np.transpose(stereo_array)



#Save to a wav file
write(f"{filename}_STEREO_CONVERT.wav", sr, stereo_out)

######VOLUME NEEDS TO BE FIXED, TOO LOW WHEN CONVERTED TO STEREO########