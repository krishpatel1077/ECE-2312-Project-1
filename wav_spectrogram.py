import matplotlib.pyplot as plt
import numpy as np
import librosa.display

# Get user input for the .wav file
filename = input("Enter the .wav file name (including extension): ")

# Load the audio file
y, sr = librosa.load(filename, sr=None)

# Generate the spectrogram
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(14, 5))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram of ' + filename)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

# Save the spectrogram as an image
output_filename = filename.replace(".wav", "_spectrogram.png")
plt.savefig(output_filename)

# Show the spectrogram
plt.show()
