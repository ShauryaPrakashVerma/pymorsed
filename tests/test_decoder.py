from pymorsed.decoder import decode
import pytest


def test_decode_hello_world():
    assert decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..", "english" ) == "HELLO WORLD"

def test_decode_numeric():
    assert decode(".---- ..--- ...-- ....- .....") == '12345'

def test_decode_alpha_numeric():
    assert decode(".... . .-.. .-.. --- / .---- ..--- ...--") == 'HELLO 123'

def test_decode_empty_string():
    assert decode("") == ""

def test_decode_invalid_character():
    with pytest.raises(ValueError) as exc:
        decode("... --- ... #")
    assert str(exc.value) == "Morse '#' not recognized"
    
def test_decode_unknown_pattern():
    with pytest.raises(ValueError):
        decode("..-.-.-")
        
def test_decode_random_string():
    with pytest.raises(ValueError):
        decode("hello")
        
def test_decode_invalid_separator():
    with pytest.raises(ValueError):
        decode("... --- ... | ...")