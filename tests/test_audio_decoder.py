import numpy as np
import pytest

from Morse_Code_Generator.audio_decoder import (
    _to_mono,
    _trim_start_auto,
    _get_envelope,
    _smooth_signal,
    _to_binary,
    _binary_to_morse,
)

def test_to_mono_stereo():
    audio = np.array([
        [1.0, 3.0],
        [2.0, 4.0]
    ])
    mono = _to_mono(audio)
    expected = np.array([2.0, 3.0])
    assert np.allclose(mono, expected)
    
    
def test_to_mono_already_mono():
    audio = np.array([1.0, 2.0, 3.0])
    mono = _to_mono(audio)
    assert np.array_equal(mono, audio)
    
    
def test_trim_start_auto():
    audio = np.array([
        0.0,
        0.0,
        0.0,
        0.02,
        0.5
    ])
    trimmed = _trim_start_auto(audio)
    expected = np.array([
        0.02,
        0.5
    ])
    assert np.array_equal(trimmed, expected)
    
    
def test_trim_start_auto_no_signal():
    audio = np.zeros(10)
    trimmed = _trim_start_auto(audio)
    assert np.array_equal(trimmed, audio)
    
    
def test_get_envelope():
    audio = np.array([
        -1.0,
        2.0,
        -3.0
    ])
    envelope = _get_envelope(audio)
    expected = np.array([
        1.0,
        2.0,
        3.0
    ])
    assert np.array_equal(envelope, expected)
    
    
def test_smooth_signal_length_preserved():
    signal = np.random.rand(100)
    smoothed = _smooth_signal(signal)
    assert len(smoothed) == len(signal)


def test_to_binary(monkeypatch):
    import matplotlib.pyplot as plt
    monkeypatch.setattr(plt, "show", lambda: None)
    signal = np.array([
        0.0,
        0.2,
        0.5,
        1.0
    ])
    binary = _to_binary(signal)
    assert binary.dtype == bool
    assert len(binary) == len(signal)
    
    
    
def test_binary_to_morse_dot():
    fs = 100
    unit = 0.1
    binary = np.concatenate([
        np.ones(5),
        np.zeros(20)
    ])
    morse = _binary_to_morse(
        binary,
        fs,
        unit
    )
    assert "." in morse
    
    
def test_binary_to_morse_dash():
    fs = 100
    unit = 0.1
    binary = np.concatenate([
        np.ones(30),
        np.zeros(20)
    ])
    morse = _binary_to_morse(
        binary,
        fs,
        unit
    )
    assert "-" in morse
    

def _binary_to_morse(binary, fs, unit):

    if len(binary) == 0:
        return ""
