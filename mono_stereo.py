from scipy.io.wavfile import write
import numpy as np
import librosa.display

filename = input("Enter the .wav file name (no extension): ")

# Load the audio file
y, sr = librosa.load((filename + '.wav'), sr=44100)

#determine period
period = 1/sr

#create stereo array
stereo_array = np.array([y,y])
#transpose array to be vertical
stereo_out = np.transpose(stereo_array)

#function to delay right channel by x number of ms

def shift_right_channel(input_array, time_ms):
    #convert time to amound of zeros, round and convert to int
    num_zeros_float = np.round(time_ms/(period*1000))
    num_zeros = num_zeros_float.astype(int)
    #append zeros to left (top) array so both have the same size
    shifted_array_channel_l = np.append(input_array,np.zeros(num_zeros))
    #shift right (bottom) channel x number of zeros
    shifted_array_channel_r = np.insert(input_array, 0, np.zeros(num_zeros))
    #combine and transpose array to be vertical
    transposed_stereo_out = np.array([shifted_array_channel_l,shifted_array_channel_r]).T
    return transposed_stereo_out

#delay right channel by average head

#delay right channel by 1ms, 10ms, and 100ms
#1ms
shift_1ms = shift_right_channel(y,1)

#10ms
shift_10ms = shift_right_channel(y,10)

#100ms
shift_100ms = shift_right_channel(y,100)


#Save all to a wav file
write(f"{filename}_STEREO_CONVERT.wav", sr, stereo_out)
write("team-stereosoundfile-1ms.wav", sr, shift_1ms)
write("team-stereosoundfile-10ms.wav", sr, shift_10ms)
write("team-stereosoundfile-100ms.wav", sr, shift_100ms)

