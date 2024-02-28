import numpy as np, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
from ipywidgets import interact
import soundfile as sf
import IPython
import time
#y, sr = librosa.load('data/58bpm.wav')
#sr = sample rate, how many audio snippets are taken per second, defaults to 22050
#audiotimes list of audioValues
audioTimes, sr = librosa.load('data/drumMetronome.wav', sr=11025)
ipd.Audio(audioTimes, rate=sr)
tempo, beat_times = librosa.beat.beat_track(y=audioTimes, sr=sr, start_bpm=80, units='time')
print("tempo: ",tempo)
print("beat times Length: ", len(beat_times))
print("beat times: ",beat_times)
sr
print("sr: ",sr)
print("audioTimes Length: ", len(audioTimes))
print("audioTimes: ",audioTimes[-100:])
# write a wav file where we trim the relevant audio:
sf.write("data/Drum2.wav", audioTimes[24000:50000], np.int32(sr))# play the generated file in notebook:
