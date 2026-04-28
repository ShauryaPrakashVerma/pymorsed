import soundfile as sf
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

from .decoder import decode


def decode_from_file(filepath):
    audio, fs = read_audio_file(filepath)
    audio = to_mono(audio)
    audio = trim_start_auto(audio)
    envelope = compute_envelope(audio)
    smoothed = smooth_signal(envelope)
    binary = to_binary(smoothed)
    WPM = 20
    unit = 1.2 / WPM
    morse = binary_to_morse(binary, fs, unit)
    print("MORSE:", morse)
    print(repr(morse))
    text = decode(morse)
    return text


def read_audio_file(filepath):
    audio, fs = sf.read(filepath)
    return audio, fs


def to_mono(audio):

    if len(audio.shape) == 2:
        audio = np.mean(audio, axis=1)

    return audio

def trim_start_auto(audio, threshold=0.01):

    indices = np.where(np.abs(audio) > threshold)[0]

    if len(indices) == 0:
        return audio

    start = indices[0]

    return audio[start:]



def trim_start(audio, fs, seconds=0.2):

    samples = int(seconds * fs)

    return audio[samples:]

def compute_envelope(audio):

    return np.abs(audio)

def smooth_signal(signal, window_size=1000):

    kernel = np.ones(window_size) / window_size

    return np.convolve(signal, kernel, mode="same")

def to_binary(signal):

    threshold = max(signal) * 0.3

    return signal > threshold

def binary_to_morse(binary, fs, unit):

    samples_per_unit = int(unit * fs)

    morse = []
    current_symbol = ""   # buffer for one letter

    current = binary[0]
    count = 0

    for value in binary:

        if value == current:
            count += 1

        else:

            duration_units = round(count / samples_per_unit)

            # -------------------------
            # SIGNAL
            # -------------------------

            if current == 1:

                if duration_units < 2:
                    current_symbol += "."

                else:
                    current_symbol += "-"

            # -------------------------
            # SILENCE
            # -------------------------

            else:

                if duration_units >= 6:

                    if current_symbol:
                        morse.append(current_symbol)
                        current_symbol = ""

                    morse.append("/")

                elif duration_units >= 2:

                    if current_symbol:
                        morse.append(current_symbol)
                        current_symbol = ""

                # else: 
                    # morse.append("#")

            current = value
            count = 1

    # flush last symbol
    if current_symbol:
        morse.append(current_symbol)

    # print("_".join(morse))
    return " ".join(morse)


def decode_from_microphone():
    fs = 44100
    duration = 5
    audio = sd.rec( int(duration * fs), samplerate = fs, channels = 1)
    sd.wait()
    print(type(audio))


def record_and_plot():

    fs = 44100
    duration = 3

    print("Recording...")

    audio = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1
    )

    sd.wait()

    print("Done")

    # Convert to 1D array
    audio = audio.flatten()

    time = np.linspace(
        0,
        duration,
        len(audio)
    )

    envelope = get_envelope(audio)
    smoothed = smooth_signal(envelope)

    
    
    plt.figure()

    threshold = 0.002

    signal = smoothed > threshold
    plt.subplot(3, 1, 1)
    plt.plot(audio)
    plt.title("Raw")

    plt.subplot(3, 1, 2)
    plt.plot(envelope)
    plt.title("Envelope")

    plt.subplot(3, 1, 3)
    plt.plot(smoothed)
    plt.title("Smoothed Envelope")
    
    plt.plot(signal)
    plt.title("Binary Signal")
    plt.show()



def get_envelope(audio):

    return np.abs(audio)

def smooth_signal(signal, window_size=500):

    kernel = np.ones(window_size) / window_size

    smoothed = np.convolve(signal, kernel, mode="same")

    return smoothed

def trim_start(audio, fs, seconds=0.2):

    samples_to_remove = int(seconds * fs)

    return audio[samples_to_remove:]


if __name__ == '__main__':
    result = decode_from_file("C:\\Users\\Shaur\\Desktop\\Morse_Code_Library_Python\\src\\Morse_Code_Generator\\output\\sos.wav")
    print(result)