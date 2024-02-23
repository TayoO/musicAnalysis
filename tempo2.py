import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
from ipywidgets import interact
#x, sr = librosa.load('data/58bpm.wav')
x, sr = librosa.load('data/StarLove.wav')
ipd.Audio(x, rate=sr)
tempo, beat_times = librosa.beat.beat_track(y=x, sr=sr, start_bpm=60, units='time')
print(tempo)
print(beat_times)
