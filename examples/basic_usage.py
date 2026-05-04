from Morse_Code_Generator.encoder import encode
from Morse_Code_Generator.decoder import decode
from Morse_Code_Generator.utils import load_language

from Morse_Code_Generator.audio_encoder import (
    morse_to_audio,
    play_audio,
    plot_waveform,
    save_audio,
)


morse = ".... . .-.. .-.. --- / -.- .- .. ... . / .... ---"

audio = morse_to_audio(morse)

play_audio(audio)
plot_waveform(audio, 44100)
save_audio(audio, "hello.wav", 44100)