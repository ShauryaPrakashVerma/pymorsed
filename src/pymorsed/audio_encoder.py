import sounddevice as sd
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

__all__ = [
    "morse_to_audio",
    "play_audio",
    "save_audio",
    "plot_waveform",
]

FS = 44100
FREQ = 700
WPM = 20

def _wpm_to_unit(wpm:int):
    if wpm <= 0:
        raise ValueError("WPM must be positive")
    unit = 1.2 / wpm
    return unit

def _generate_tone(freq, duration):
    t = np.linspace(0 , duration, int(FS * duration), False)
    tone = np.sin(2 * np.pi * freq * t)
    return tone

def _generate_silence(duration):
    return np.zeros(int(FS * duration))

def morse_to_audio(morse, wpm=WPM, frequency=FREQ):

    unit = _wpm_to_unit(wpm)
    audio_parts = []
    for symbol in morse:

        if symbol == ".":
            audio_parts.append(_generate_tone(frequency, unit))
            audio_parts.append(_generate_silence(unit))

        elif symbol == "-":
            audio_parts.append(_generate_tone(frequency, 3 * unit))
            audio_parts.append(_generate_silence(unit))

        elif symbol == " ":
            audio_parts.append(_generate_silence(2 * unit))

        elif symbol == "/":
            audio_parts.append(_generate_silence(6 * unit))

    audio_parts.append(_generate_silence(10 * unit))
    return np.concatenate(audio_parts)
            
    
def play_audio(audio):
    sd.play(audio, FS)
    sd.wait()


def save_audio(audio, filename, fs):
    """
    Save audio array to a file.

    Parameters:
        audio : numpy array
        filename : str (e.g. 'morse.wav')
        fs : sample rate
    """
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    path = output_dir / filename
    sf.write(path, audio, fs)
    print("Saving to:", os.getcwd())


def plot_waveform(audio, fs):
    duration = len(audio) / fs
    time = np.linspace(0, duration, len(audio))
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio)
    plt.title("Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

