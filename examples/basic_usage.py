from pymorsed.encoder import encode
from pymorsed.decoder import decode
from pymorsed.utils import load_language

from pymorsed.audio_encoder import (
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