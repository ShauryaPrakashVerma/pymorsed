import soundfile as sf
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

from .decoder import decode


def decode_from_file(filepath):
    """
    Decode a Morse code audio file into text.

    Parameters
        filepath : str or pathlib.Path
            Path to the input audio file.

    Output
        str : Decoded text message.
    """
    audio, fs = _read_audio_file(filepath)
    audio = _to_mono(audio)
    return _decode_audio(audio, fs)



def _decode_audio(audio, fs, wpm=20):

    audio = _trim_start_auto(audio)
    envelope = _get_envelope(audio)
    smoothed = _smooth_signal(envelope)
    binary = _to_binary(smoothed)
    unit = 1.2 / wpm
    morse = _binary_to_morse(
        binary,
        fs,
        unit
    )
    return decode(morse)



# TODO (v0.2.0):
# Implement microphone-based Morse decoding.
# Challenges:
# - Automatic WPM estimation
# - Noise filtering
# - Robust threshold detection
# - Hardware-independent testing


def decode_from_microphone(duration=5):
    raise NotImplementedError(
        "Microphone decoding will be added in v0.2.0."
    )
    # fs = 44100
    # audio = sd.rec(
    #     int(duration * fs),
    #     samplerate=fs,
    #     channels=1
    # )
    # sd.wait()
    # audio = audio.flatten()
    # return _decode_audio(audio, fs)


def _read_audio_file(filepath):
    audio, fs = sf.read(filepath)
    return audio, fs


def _to_mono(audio):
    if len(audio.shape) == 2:
        audio = np.mean(audio, axis=1)
    return audio


def _trim_start_auto(audio, threshold=0.01):
    indices = np.where(np.abs(audio) > threshold)[0]
    if len(indices) == 0:
        return audio
    start = indices[0]
    return audio[start:]


def _smooth_signal(signal, window_size=50):
    kernel = np.ones(window_size) / window_size
    return np.convolve(signal, kernel, mode="same")


def _to_binary(signal):
    threshold = np.max(signal) * 0.3
    binary = signal > threshold
    return binary


def _binary_to_morse(binary, fs, unit):
    samples_per_unit = unit * fs
    morse = []
    current_symbol = ""   # This builds a single letter (e.g., "...")
    current = binary[0]
    count = 0

    for value in binary:
        if value == current:
            count += 1
        else:
            duration_units = count / samples_per_unit
            if current == 1:
                if duration_units < 2.0:
                    current_symbol += "."
                else:
                    current_symbol += "-"

            else:
                if duration_units < 1.5: 
                    pass
                elif duration_units >= 1.5 and duration_units < 5.0:
                    if current_symbol:
                        morse.append(current_symbol)
                        current_symbol = ""
                elif duration_units >= 5.0:
                    if current_symbol:
                        morse.append(current_symbol)
                        current_symbol = ""
                    morse.append("/")

            current = value
            count = 1

    if current_symbol:
        morse.append(current_symbol)

    return " ".join(morse)



def _record_and_plot(span):
    fs = 44100
    duration = span

    print("Recording...")

    audio = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1
    )
    sd.wait()
    print("Done")
    audio = audio.flatten()
    time = np.linspace(
        0,
        duration,
        len(audio)
    )
    envelope = _get_envelope(audio)
    smoothed = _smooth_signal(envelope)
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


def _get_envelope(audio):
    return np.abs(audio)