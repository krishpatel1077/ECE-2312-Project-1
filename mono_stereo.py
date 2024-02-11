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

#measurements in m (delay)
m_kyle = 0.095493
m_krish = 0.095493
m_ana = 0.0923099

#delays calculated (s)
speed_sound = 343
delay_kyle = m_kyle/speed_sound;
delay_krish = m_krish/speed_sound;
delay_ana = m_ana/speed_sound;

avg_delay = (delay_ana + delay_kyle + delay_krish)/3;
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
    stereo_out_notranspose = np.array([shifted_array_channel_l,shifted_array_channel_r])
    transposed_stereo_out = np.transpose(stereo_out_notranspose)
    return transposed_stereo_out, stereo_out_notranspose

def attenuate_right_channel(input_array, db_amount, mono_stereo):
    #set up a case statement for each attenuation factor
    factor = 0
    if (db_amount == '-3'):
        factor = 0.5
    elif (db_amount == '-6'):
        factor = 0.25
    elif (db_amount == '-1.5'):
        factor = 0.75
    else:
        print("ERROR")
    
    #if its in mono mode
    if mono_stereo == 1:
        factor_array = input_array * factor
        #create array
        stereo_array = np.array([input_array,factor_array])
        #transpose array to be vertical
        stereo_out = np.transpose(stereo_array)    
    
    #if input array is stereo, only take the right channel to attenuate and leave the left untouched
    elif mono_stereo ==0:
        factor_array = input_array[1] * factor
        #create array
        stereo_array = np.array([input_array[0],factor_array])
        #transpose array to be vertical
        stereo_out = np.transpose(stereo_array)
    
    return  stereo_out  
    
#delay right channel by average head
shift_avg_delay, avg_array_untransposed = shift_right_channel(y, avg_delay)

#delay right channel by 1ms, 10ms, and 100ms
#1ms
shift_1ms = shift_right_channel(y,1)

#10ms
shift_10ms = shift_right_channel(y,10)

#100ms
shift_100ms = shift_right_channel(y,100)

#Attenuate 0ms stereo by -1.5, -3, -6db
#-1.5db
shift_1_5db = attenuate_right_channel(y,'-1.5', 1)

#10ms
shift_3_db = attenuate_right_channel(y,'-3', 1)

#100ms
shift_6_db = attenuate_right_channel(y,'-6', 1)

#Attenuate averagedelay stereo by -1.5, -3, -6db
#-1.5db
shift_avgdelay_1_5db = attenuate_right_channel(avg_array_untransposed,'-1.5', 0)

#10ms
shift_avgdelay_3_db = attenuate_right_channel(avg_array_untransposed,'-3', 0)

#100ms
shift_avgdelay_6_db = attenuate_right_channel(avg_array_untransposed,'-6',0)


#Save all to a wav file
write(f"{filename}_STEREO_CONVERT.wav", sr, stereo_out)
write("team-stereosoundfile-1ms.wav", sr, shift_1ms[0])
write("team-stereosoundfile-10ms.wav", sr, shift_10ms[0])
write("team-stereosoundfile-100ms.wav", sr, shift_100ms[0])

write("team-stereosoundfile-0ms-1_5db.wav", sr, shift_1_5db)
write("team-stereosoundfile-0ms-3_db.wav", sr, shift_3_db)
write("team-stereosoundfile-0ms-6_db.wav", sr, shift_6_db)

#team member delay version
write("team-ear-measurements-avg-delay.wav", sr, shift_avg_delay)
write("team-ear-measurements-avg-delay-1_5db.wav", sr, shift_avgdelay_1_5db)
write("team-ear-measurements-avg-delay.wav-3_db.wav", sr, shift_avgdelay_3_db)
write("team-ear-measurements-avg-delay.wav-6_db.wav", sr, shift_avgdelay_6_db)