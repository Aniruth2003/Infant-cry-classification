
import pyaudio
import wave
import time

# set parameters for audio recording
FORMAT = pyaudio.paInt16
RATE = 44100
CHANNELS = 1
CHUNK = 1024
RECORD_SECONDS = 10

# initialize PyAudio object
audio = pyaudio.PyAudio()

# create a stream for recording
stream = audio.open(format=FORMAT, rate=RATE, channels=CHANNELS, input=True, frames_per_buffer=CHUNK)

# loop to record audio for 5 seconds per minute
while True:
    # create a new WAV file for each recording
    filename = 'recording_' + str(int(time.time())) + '.wav'
    frames = []
    # record audio for 5 seconds
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
	frames.append(data)
# save the recording to a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
# wait for 55 seconds before recording again
time.sleep(55)
