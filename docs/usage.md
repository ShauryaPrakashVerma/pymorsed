# Quick Start

The recommended way is to import directly from the package namespace.

```python
from pymorsed import encode, decode, morse_to_audio

morse = encode("HELLO")
print(morse)

text = decode(morse)
print(text)
```

---

## Import Individual Modules

You can also import functionality from specific modules.

### Text Encoding

```python
from pymorsed.encoder import encode

morse = encode("HELLO")
print(morse)
```

### Text Decoding

```python
from pymorsed.decoder import decode

text = decode(".... . .-.. .-.. ---")
print(text)
```

### Audio Encoding

```python
from pymorsed.audio_encoder import morse_to_audio

morse_to_audio("... --- ...")

```

### Audio Decoding

```python
from pymorsed.audio_decoder import decode_from_file

text = decode_from_file("sos.wav")
print(text)
```

---

## Import the Entire Package

```python
import pymorsed

morse = pymorsed.encode("HELLO")
text = pymorsed.decode(morse)
```

This approach is useful when working with multiple functions from the library.

---

