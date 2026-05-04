import os
import numpy as np
import pytest

from Morse_Code_Generator.audio_encoder import (
    morse_to_audio,
    save_audio,
)


# BASIC FUNCTIONALITY
def test_morse_to_audio_returns_numpy_array():
    """Audio output should be a numpy array."""

    morse = "... --- ..."
    audio = morse_to_audio(morse)
    assert isinstance(audio, np.ndarray)


def test_morse_to_audio_not_empty():
    """Generated audio should contain samples."""

    audio = morse_to_audio("...")
    assert len(audio) > 0


def test_deterministic_audio_output():
    """Same input should always produce identical output."""

    morse = "... --- ..."

    audio1 = morse_to_audio(morse)
    audio2 = morse_to_audio(morse)
    assert np.array_equal(audio1, audio2)

    
def test_dot_vs_dash_length():
    dot = morse_to_audio(".")
    dash = morse_to_audio("-")

    assert len(dash) > len(dot)


def test_non_empty_output():
    audio = morse_to_audio("...")
    assert len(audio) > 0

# TIMING / WPM BEHAVIOR
def test_wpm_affects_audio_length():
    """Lower WPM should produce longer audio."""

    morse = "... --- ..."

    slow_audio = morse_to_audio(morse, wpm=10)
    fast_audio = morse_to_audio(morse, wpm=30)
    assert len(slow_audio) > len(fast_audio)


def test_invalid_wpm_raises_error():
    """WPM must be positive."""

    with pytest.raises(ValueError):
        morse_to_audio("...", wpm=0)


def test_high_wpm_still_generates_audio():
    """Very fast speed should still produce valid output."""

    audio = morse_to_audio("...", wpm=40)
    assert len(audio) > 0


def test_low_wpm_still_generates_audio():
    """Very slow speed should still produce valid output."""

    audio = morse_to_audio("...", wpm=5)
    assert len(audio) > 0




# FREQUENCY / SIGNAL PROPERTIES
def test_custom_frequency_parameter():
    """Changing frequency should still produce valid audio."""

    audio = morse_to_audio("...", frequency=1000)
    assert len(audio) > 0


def test_audio_amplitude_range():
    """Signal amplitude should stay within valid bounds."""

    audio = morse_to_audio("...")
    assert np.max(audio) <= 1
    assert np.min(audio) >= -1



# MORSE STRUCTURE BEHAVIOR
def test_word_gap_longer_than_letter_gap():
    """Word gap should create longer silence."""

    audio_letter_gap = morse_to_audio("... ...")
    audio_word_gap = morse_to_audio(".../...")
    assert len(audio_word_gap) > len(audio_letter_gap)


def test_empty_morse_input():
    """Empty input should still return valid audio."""
    audio = morse_to_audio("")
    assert isinstance(audio, np.ndarray)




# FILE OUTPUT
def test_save_audio_creates_file():
    morse = "..."
    audio = morse_to_audio(morse)
    filename = "test_audio.wav"
    save_audio(audio, filename, 44100)
    expected_path = os.path.join("output", filename)
    assert os.path.exists(expected_path)
    
    # cleanup
    os.remove(expected_path)




# STABILITY TEST
def test_large_input_stability():
    """Large Morse string should not crash."""
    morse = "... --- ... " * 50
    audio = morse_to_audio(morse)
    assert len(audio) > 0