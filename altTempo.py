import aubio
import wave
import struct
import math

# Function to calculate BPM of a song
def calculate_bpm(audio_path):
    # Open the audio file
    audio = aubio.source(audio_path)
    
    # Create a tempo detector
    tempo_detector = aubio.tempo("default", audio.samplerate)
    
    # Run the tempo detector on the audio
    total_frames = 0
    while True:
        samples, read = audio()
        if read < audio.hop_size:
            break
        tempo = tempo_detector(samples)
        if tempo:
            return tempo[0]

    return None

# Function to generate a metronome sound
def generate_metronome(bpm, duration=60):
    # Calculate the sample rate and the number of frames
    sample_rate = 44100  # CD quality audio
    num_frames = int(duration * sample_rate)

    # Open a new wave file
    output_file = wave.open(f"metronome_{bpm}bpm.wav", "w")
    output_file.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))

    # Calculate the number of frames per beat
    frames_per_beat = int(sample_rate * 60 / bpm)

    # Generate the metronome sound
    for _ in range(int(duration)):
        for i in range(frames_per_beat):
            # Generate a simple square wave (alternating between +1 and -1)
            value = struct.pack('<h', int(32767 * math.sin(math.pi * 2 * i * 440 / sample_rate)))
            output_file.writeframes(value)

    # Close the file
    output_file.close()

    print(f"Metronome sound generated at {bpm} BPM and saved to metronome_{bpm}bpm.wav")

# Path to the audio file
audio_path = "data/StarLove.wav"  # Replace with the path to your audio file

# Calculate BPM of the song
bpm = calculate_bpm(audio_path)

if bpm:
    print(f"BPM of the song: {bpm}")
    generate_metronome(bpm)
else:
    print("Failed to calculate BPM of the song.")
