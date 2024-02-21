import numpy as np
import scipy.io.wavfile as wavfile
import librosa
import IPython
# load file and extract tempo and beats:
[Fs, s] = wavfile.read('data/StarLove.wav')
tempo, beats = librosa.beat.beat_track(y=s.astype('float'), sr=Fs, units="time")
beats -= 0.05
# add small 220Hz sounds on the 2nd channel of the song ON EACH BEAT
s = s.reshape(-1, 1)
s = np.array(np.concatenate((s, np.zeros(s.shape)), axis=1))
for ib, b in enumerate(beats):
    t = np.arange(0, 0.2, 1.0 / Fs)
    amp_mod = 0.2 / (np.sqrt(t)+0.2) - 0.2
    amp_mod[amp_mod < 0] = 0
    x = s.max() * np.cos(2 * np.pi * t * 220) * amp_mod
    s[int(Fs * b):
      int(Fs * b) + int(x.shape[0]), 1] = x.astype('int16')
# write a wav file where the 2nd channel has the estimated tempo:
wavfile.write("data/StarLove_with_tempo.wav", Fs, np.int16(s))    
# play the generated file in notebook:
IPython.display.display(IPython.display.Audio("data/StarLove_with_tempo.wav"))
