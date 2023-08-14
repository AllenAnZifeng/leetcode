import numpy as np
import wave
import matplotlib.pyplot as plt


def read_wav_file(file_path):
    with wave.open(file_path, 'rb') as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        audio_data = wf.readframes(n_frames)

    audio_array = np.frombuffer(audio_data, dtype=np.int16)

    # 如果音频是立体声，只取一个通道（例如左通道）的数据
    if n_channels == 2:
        audio_array = audio_array[::2]

    return audio_array, framerate


def plot_fft(audio_array, sampling_rate):
    n = len(audio_array)
    fft_values = np.fft.rfft(audio_array)
    fft_frequencies = np.fft.rfftfreq(n, d=1 / sampling_rate)

    plt.plot(fft_frequencies, np.abs(fft_values))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('FFT of the Audio Signal')
    plt.show()


if __name__ == '__main__':
    # f = [500, 1000, 2000, 3000, 4000, 6000, 8000]
    # audio_array = []
    # sampling_rate = 0
    # for i in range(len(f)):
    #     wav_file_path = f'sine_wave_{f[i]}Hz_left_channel.wav'
    #     temp_audio_array, sampling_rate = read_wav_file(wav_file_path)
    #     audio_array.extend(temp_audio_array)
    #
    # plot_fft(audio_array, sampling_rate)

    wav_file_path = 'fm_signal.wav'
    audio_array, sampling_rate = read_wav_file(wav_file_path)
    plot_fft(audio_array, sampling_rate)
