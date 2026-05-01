from Morse_Code_Generator.encoder import encode
import pytest


def test_encode_hello_world():
    result = encode("Hello World", "english")
    assert result == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

def test_encode_numeric_message():
    result = encode("12345", "english")
    assert result == ".---- ..--- ...-- ....- ....."

def test_encode_mixed_message():
    result = encode("Hello 123", "english")
    assert result == ".... . .-.. .-.. --- / .---- ..--- ...--"

def test_encode_empty_string():
    result = encode("", language="english")
    assert result == ""

def test_encode_invalid_character():
    with pytest.raises(ValueError):
        encode("Hello#", language="english")