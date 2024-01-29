import matplotlib.pyplot as plt
import numpy as np
import librosa.display

# Get user input for the .wav file
filename = input("Enter the .wav file name (including extension): ")

# Load the audio file
y, sr = librosa.load(filename, sr=44100)

# Generate the spectrogram
D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=512)), ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(14, 5))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='linear')
# Set maximum Y value to 8000Hz
ax = plt.gca() #get current axes
ax.set_ylim([0, 8001])
# Get current min and max on the y axis and set them to the limits with step of 1000hz
start, end = ax.get_ylim()
ax.set_yticks(np.arange(start, end, 1000))

plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram of ' + filename)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

# Save the spectrogram as an image
output_filename = filename.replace(".wav", "_spectrogram.png")
plt.savefig(output_filename)

# Show the spectrogram
plt.show()
