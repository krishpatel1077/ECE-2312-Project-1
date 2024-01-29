import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import IPython.display as ipd

# Define Sampling Rate or Frequency in Hz
sr = 44100

# Get user input for filename and duration
filename = input("Enter the filename (without extension): ")
duration = float(input("Enter the duration of recording (in seconds): "))
Mono_Stereo = int(input("Mono =1 | Stereo =2: "))

# Start audio recording
recording = sd.rec(int(duration*sr), samplerate=sr, channels=1)
# Record with a mono or stereo channel microphone
# Record audio for the given duration
print("Recording...............")
sd.wait()
# Write it to a file

if Mono_Stereo == 1:
    write(f"{filename}_MONO.wav", sr, recording)
elif Mono_Stereo == 2:
    write(f"{filename}_STEREO.wav", sr, recording)

# Plot the recorded audio
plt.figure(figsize=(14, 5))

librosa.display.waveshow(np.array(recording[:, 0]), sr=sr, color="blue")
plt.title('Recorded Audio')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Save the plot as an image
if Mono_Stereo == 1:
    plt.savefig(f"{filename}_soundwave_MONO.png")
elif Mono_Stereo == 2:
    plt.savefig(f"{filename}_soundwave_STEREO.png")

# Show the plot
plt.show()

# Play the recorded audio
ipd.Audio(f"{filename}.wav")
