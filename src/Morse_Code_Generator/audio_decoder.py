import soundfile as sf
import numpy as np
import sounddevice as sd

import matplotlib.pyplot as plt

def decode_from_file():
    
    audio, fs = sf.read("C:\\Users\\Shaur\\Desktop\\Morse_Code_Library_Python\\src\\Morse_Code_Generator\\output\\sos.wav")
    print(type(audio))
    print(audio.round(3))
    print(len(audio))
    print(fs)
    

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

record_and_plot()
# decode_from_file()