import numpy as np, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
from ipywidgets import interact
import soundfile as sf
import IPython
#x, sr = librosa.load('data/58bpm.wav')
x, sr = librosa.load('data/StarLove.wav')
ipd.Audio(x, rate=sr)
tempo, beat_times = librosa.beat.beat_track(y=x, sr=sr, start_bpm=60, units='time')
print(tempo)
print(beat_times)
s=sr
Fs=x
# write a wav file where the 2nd channel has the estimated tempo:
sf.write("data/StarLove_with_tempo.wav", Fs, np.int16(s))
# play the generated file in notebook:
IPython.display.display(IPython.display.Audio("data/StarLove_with_tempo.wav"))
