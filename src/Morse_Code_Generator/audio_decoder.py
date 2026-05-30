import soundfile as sf
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

from .decoder import decode


def decode_from_file(filepath):
    audio, fs = _read_audio_file(filepath)
    audio = _to_mono(audio)
    audio = _trim_start_auto(audio)
    envelope = _get_envelope(audio)
    smoothed = _smooth_signal(envelope)
    binary = _to_binary(smoothed)
    WPM = 20
    unit = 1.2 / WPM
    morse = _binary_to_morse(binary, fs, unit)
    text = decode(morse)
    return text


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
    # plt.figure()
    # plt.plot(signal)
    # plt.axhline(threshold)
    # plt.title("Signal with Threshold")
    # plt.show()
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


if __name__ == "__main__":
    filepath = r"C:\\Users\\Shaur\\Desktop\\Morse_Code_Library_Python\\src\\Morse_Code_Generator\\output\\shaurya.wav"

    print("Reading audio...")
    audio, fs = _read_audio_file(filepath)
    print(f"Sample Rate: {fs}")
    print(f"Audio Shape: {audio.shape}")

    audio = _to_mono(audio)
    print(f"After mono conversion: {audio.shape}")

    audio = _trim_start_auto(audio)
    print(f"After trimming: {len(audio)} samples")

    envelope = _get_envelope(audio)
    print(f"Envelope Length: {len(envelope)}")

    smoothed = _smooth_signal(envelope)
    print(f"Smoothed Length: {len(smoothed)}")

    binary = _to_binary(smoothed)
    print(f"Binary Length: {len(binary)}")

    unit = 1.2 / 20

    morse = _binary_to_morse(binary, fs, unit)
    print(f"Morse Decoded: {morse}")

    text = decode(morse)
    print(f"Text Decoded: {text}")
    
    
    
    
    decode_from_microphone()
    
    # print("=" * 50)
    # print("Testing record_and_plot()")
    # print("Speak into the microphone for 3 seconds...")
    # print("=" * 50)

    # try:
    #     record_and_plot()

    #     print("\nChecks:")
    #     print("[✓] Audio recording completed")
    #     print("[✓] Envelope computed")
    #     print("[✓] Signal smoothed")
    #     print("[✓] Binary signal generated")
    #     print("[✓] Plots displayed")

    # except Exception as e:
    #     print(f"\n[✗] Test failed: {e}")