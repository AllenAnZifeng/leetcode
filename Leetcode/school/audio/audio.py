import numpy as np
import pyaudio
import wave

# set the sample rate and duration
sample_rate = 44100
duration = 5 # in seconds

# generate the sine wave
frequency = 500 # in Hz
t = np.linspace(0, duration, int(sample_rate * duration), False)
note = np.sin(frequency * t * 2 * np.pi)

# create a PyAudio object
p = pyaudio.PyAudio()

# open a stream
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                output=True)

# # play the sine wave
# stream.write(note.astype(np.float32).tobytes())

# save the sine wave to a WAV file
file_name = f"{frequency}.wav"
with wave.open(file_name, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paFloat32))
    wf.setframerate(sample_rate)
    wf.writeframes(note.astype(np.float32).tobytes())

# play the sine wave from the WAV file
with wave.open(file_name, "rb") as wf:
    stream.write(wf.readframes(wf.getnframes()))

# close the stream and terminate the PyAudio object
stream.stop_stream()
stream.close()
p.terminate()