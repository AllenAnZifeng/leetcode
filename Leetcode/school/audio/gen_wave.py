import numpy as np
import wave
import struct

f = [500,1000,2000,3000,4000,6000,8000]
# CHANNEL = 'left'
CHANNEL = 'right'
for i in range(len(f)):

    # 参数设置
    duration = 1  # 时长 (秒)
    freq = f[i]  # 频率 (赫兹)
    sampling_rate = 44100  # 采样率 (赫兹)
    amplitude = 32767  # 振幅 (16位PCM)
    output_file = f'sine_wave_{freq}Hz_{CHANNEL}_channel.wav'  # 输出文件名

    # 生成正弦波
    t = np.linspace(0, duration, sampling_rate * duration, endpoint=False)


    # 将浮点数转换为整数以适应PCM格式
    if CHANNEL == 'left':
        left_channel = amplitude * np.sin(2 * np.pi * freq * t)
        right_channel = np.zeros_like(left_channel)
        left_channel_int = left_channel.astype(np.int16)
        right_channel_int = right_channel.astype(np.int16)
    else:
        left_channel = np.zeros_like(t)
        right_channel = amplitude * np.sin(2 * np.pi * freq * t)
        left_channel_int = left_channel.astype(np.int16)
        right_channel_int = right_channel.astype(np.int16)


    # 写入wav文件
    with wave.open(output_file, 'wb') as wf:
        # 设置wav参数
        wf.setnchannels(2)  # 双声道
        wf.setsampwidth(2)  # 16位PCM
        wf.setframerate(sampling_rate)  # 采样率

        # 写入数据
        for left_sample, right_sample in zip(left_channel_int, right_channel_int):
            wf.writeframesraw(struct.pack('<h', left_sample))
            wf.writeframesraw(struct.pack('<h', right_sample))

    print(f"生成的音频文件已保存为 {output_file}")
