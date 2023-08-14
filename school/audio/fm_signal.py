import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

# Parameters
duration = 3  # duration of the signal in seconds
sample_rate = 44100  # samples per second
carrier_freq = 100  # carrier frequency in Hz
min_mod_freq = 100  # minimum modulating frequency in Hz
max_mod_freq = 1000  # maximum modulating frequency in Hz
pure_tone_freq = 500  # pure tone frequency in Hz
wav_filename = f'stereo_signal_{pure_tone_freq}.wav'
# Time array
t = np.arange(0, duration, 1/sample_rate)

# Modulating signal (linearly varying frequency)
mod_signal = np.linspace(min_mod_freq, max_mod_freq, len(t))
mod_signal = np.sin(2 * np.pi * mod_signal * t)

# FM signal (right channel)
fm_signal = np.sin(2 * np.pi * carrier_freq * t + mod_signal)

# Normalize the FM signal to the range [-1, 1]
fm_signal /= np.max(np.abs(fm_signal))

# Pure tone signal (left channel)
pure_tone_signal = np.sin(2 * np.pi * pure_tone_freq * t)

# Combine left and right channels as a stereo signal
stereo_signal = np.column_stack((pure_tone_signal, fm_signal))
# stereo_signal = np.column_stack((pure_tone_signal, pure_tone_signal))

# Save the stereo signal as a WAV file
wavfile.write(wav_filename, sample_rate,  (stereo_signal * 32767).astype(np.int16))

from pydub import AudioSegment



# Convert the WAV file to an MP3 file
audio = AudioSegment.from_wav(wav_filename)
mp3_filename = f'stereo_signal_{pure_tone_freq}.mp3'
audio.export(mp3_filename, format="mp3")

# # Plot the left and right channels
# fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
# ax1.plot(t, pure_tone_signal)
# ax1.set_ylabel('Amplitude')
# ax1.set_title('Left Channel: 500 Hz Pure Tone')
#
# ax2.plot(t, fm_signal)
# ax2.set_xlabel('Time (s)')
# ax2.set_ylabel('Amplitude')
# ax2.set_title('Right Channel: FM Signal')
#
# plt.show()
