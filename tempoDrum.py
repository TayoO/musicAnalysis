import numpy as np, scipy, matplotlib.pyplot as plt
import librosa, librosa.display
from ipywidgets import interact
import soundfile as sf
import IPython
import time
import wave

#sr = sample rate, how many audio snippets are taken per second, defaults to 22050
#audiotimes list of audioValues
audioTimes, sr = librosa.load('data/drumMetronome.wav', sr=11025)
tempo, beat_times = librosa.beat.beat_track(y=audioTimes, sr=sr, start_bpm=80, units='time')

#rough trim of the data based on the capturing the first drum beat 
#and 3 more metronome hits and the next beat after that to be used as a marker

drumTimes= audioTimes[24000:62000]

# write a wav file where we trim the relevant audio:
sf.write("data/drum2.wav", drumTimes, np.int32(sr))
'''
atTrim=[]
start=0
stop=len(drumTimes)-1
while drumTimes[start] ==0:
  start+=1
while drumTimes[stop] ==0:
  stop-=1
atTrim = drumTimes[start:stop]
'''
tempoDrum, beat_timeD = librosa.beat.beat_track(y=drumTimes, sr=sr, start_bpm=80, units='time')
print("Drum tempo: ",tempoDrum)
print("Drum beat times Length: ", len(beat_timeD))
#print("beat times: ",beat_timeD)
#print("sr: ",sr)
#print("audioTimes Length: ", len(atTrim))
#print("audioTime start: ",audioTimes[0:100])
#print("audioTime end: ",audioTimes[-1:-100:-1])
#print("audioTimes: ",audioTimes[::1000])
audioTimeS, sr = librosa.load('data/thatManOfMine.wav)', sr=11025)

tempoSong, beat_timeS = librosa.beat.beat_track(y=audioTimeS, sr=sr, start_bpm=80, units='time')
print("Song tempo: ",tempoSong)
print("Song beat times Length: ", len(beat_timeS))
#print("beat times: ",beat_timeS)

#Modify drum beat to original song
CHANNELS = 1
swidth = 2
Change_RATE = tempoSong/tempoDrum

spf = wave.open('data/drum2.wav', 'rb')
RATE=spf.getframerate()
signal = spf.readframes(-1)

wf = wave.open('data/drumChanged.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(swidth)
wf.setframerate(RATE*Change_RATE)
wf.writeframes(signal)
wf.close()


#display new beat
audioTimeC, sr = librosa.load('data/drumChanged.wav', sr=11025)
tempoChanged, beat_timeC = librosa.beat.beat_track(y=audioTimeC, sr=sr, start_bpm=80, units='time')
print("Modified Drum tempo: ",tempoChanged)
print("first 4 beat times of the song", beat_timeS[0:4])
print("Beat times of drum", beat_timeC)
print("audioTimes of song: ", audioTimeS)
print("audioTimes of modified beat: ", audioTimeC)
#adjust drum beat to start at the same time as the original song
frameDif= round(sr*(beat_timeS[0]-beat_timeC[0]))
print ("Differences of frames between first beats: ", frameDif)
audioZeros=np.zeros(frameDif)
print(len(audioZeros))
audioSync=np.append(audioZeros,audioTimeC)
print(len(audioSync))
print("--------------------------------")
print("audio length of drums", len(audioTimeC))
print("--------------------------------")
print("audioSync: ",len(audioSync))
print("--------------------------------")
tempoSync, beat_timeSync = librosa.beat.beat_track(y=audioSync, sr=sr, start_bpm=80, units='time')
print("Beat time original", beat_times)
print("Beat time D", beat_timeD)
print("Beat time changed", beat_timeC)
print("Beat time sync: ", beat_timeSync)
print("Original song beats: ", beat_timeS[0:4])
beatInterval=((1/tempoSync)*60)
lastBeat=0
for beat in beat_timeS:
  print (beatInterval -beat +lastBeat)
  lastBeat=beat
print(beatInterval+beat_timeSync[1])


