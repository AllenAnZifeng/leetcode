import os
import numpy as np
import soundfile as sf
import sounddevice as sd
from gtts import gTTS

# Normal: </= 6 dB
# Mild: 6.8 – 10.0
# Moderate: 10.8 – 14.8
# Severe: 15.6 – 19.6
# Profound: >20 dB

# Constants
SAMPLE_RATE = 24000  # Sample rate in Hz
DURATION = 1  # Duration of each digit in seconds
NOISE_LEVEL = 0.001  # Adjust this value for desired noise level (0 to 1)

def calculate_snr(signal, noise):
    signal_power = np.mean(np.square(signal))
    noise_power = np.mean(np.square(noise))
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Generate a digit sound
def generate_digit(digit, sample_rate):
    tts = gTTS(str(digit), lang='en', tld='com')
    digit_file = f'digit_{digit}.wav'
    tts.save(digit_file)
    digit_sound, _ = sf.read(digit_file, dtype='float32')
    os.remove(digit_file)
    return digit_sound

# Generate white noise
def generate_noise(duration, sample_rate, noise_level):
    noise = np.random.normal(0, noise_level, int(duration * sample_rate))
    return noise

# Generate a hearing test sequence with noise
def generate_sequence(digits, sample_rate, noise_level):
    sequences = []
    snrs = []

    for digit in digits:
        digit_sound = generate_digit(digit, sample_rate)
        noise = generate_noise(len(digit_sound) / sample_rate, sample_rate, noise_level)
        sequence = digit_sound + noise
        sequences.append(sequence)
        snr = calculate_snr(digit_sound, noise)
        snrs.append(snr)

    # Concatenate sequences and resample if necessary
    full_sequence = np.concatenate(sequences)
    if SAMPLE_RATE != 24000:
        full_sequence = sd.resample(full_sequence, SAMPLE_RATE, 24000)

    return full_sequence, snrs

# Main function
def main():
    digits = [np.random.randint(0, 10) for _ in range(3)]  # Generate 3 random digits
    print("Generated Digits:", digits)

    sequence, snrs = generate_sequence(digits, SAMPLE_RATE, NOISE_LEVEL)
    print("SNRs for each digit (dB):", snrs)

    name = ''.join([str(digit) for digit in digits])
    sf.write(f'{name}-{NOISE_LEVEL}.wav', sequence, SAMPLE_RATE)  # Save the generated audio sequence to a file
    print(f"Audio saved as {name}-{NOISE_LEVEL}.wav")

    sd.play(sequence, samplerate=SAMPLE_RATE)
    sd.wait()

if __name__ == "__main__":
    for i in range(5):
        main()
