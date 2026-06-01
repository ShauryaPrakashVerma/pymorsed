# API Reference

This page documents all public functions provided by the `pymorsed` library.

---

# Encoder Module

```python
from pymorsed.encoder import encode
```

## `encode(text, language="english")`

Converts plain text into Morse code.

### Parameters

| Parameter  | Type  | Description                                        |
| ---------- | ----- | -------------------------------------------------- |
| `text`     | `str` | Text to encode into Morse code                     |
| `language` | `str` | Language mapping to use (`"english"`, `"russian"`) |

### Returns

```python
str
```

Morse code representation of the input text.

### Example

```python
from pymorsed.encoder import encode

morse = encode("HELLO")
print(morse)
```

Output:

```text
.... . .-.. .-.. ---
```

---

# Decoder Module

```python
from pymorsed.decoder import decode
```

## `decode(morse, language="english")`

Converts Morse code back into plain text.

### Parameters

| Parameter  | Type  | Description                           |
| ---------- | ----- | ------------------------------------- |
| `morse`    | `str` | Morse code string                     |
| `language` | `str` | Language mapping used during decoding |

### Returns

```python
str
```

Decoded text.

### Example

```python
from pymorsed.decoder import decode

text = decode(".... . .-.. .-.. ---")
print(text)
```

Output:

```text
HELLO
```

---

# Audio Encoder Module

```python
from pymorsed.audio_encoder import (
    morse_to_audio,
    play_audio,
    save_audio,
    plot_waveform
)
```

---

## `morse_to_audio(morse, wpm=20, frequency=700)`

Generates a Morse code audio signal as a NumPy array.

### Parameters

| Parameter   | Type  | Description                            |
| ----------- | ----- | -------------------------------------- |
| `morse`     | `str` | Morse code string                      |
| `wpm`       | `int` | Transmission speed in words per minute |
| `frequency` | `int` | Tone frequency in Hertz                |

### Returns

```python
numpy.ndarray
```

Generated waveform.

### Example

```python
from pymorsed.audio_encoder import morse_to_audio

audio = morse_to_audio("... --- ...")
```

---

## `play_audio(audio)`

Plays a generated Morse code waveform through the system speakers.

### Parameters

| Parameter | Type            |
| --------- | --------------- |
| `audio`   | `numpy.ndarray` |

### Returns

None

### Example

```python
from pymorsed.audio_encoder import *

audio = morse_to_audio("... --- ...")
play_audio(audio)
```

---

## `save_audio(audio, filename, fs=44100)`

Saves a Morse waveform as a WAV file.

### Parameters

| Parameter  | Type            | Description     |
| ---------- | --------------- | --------------- |
| `audio`    | `numpy.ndarray` | Audio waveform  |
| `filename` | `str`           | Output filename |
| `fs`       | `int`           | Sample rate     |

### Returns

None

### Example

```python
from pymorsed.audio_encoder import *

audio = morse_to_audio("... --- ...")
save_audio(audio, "sos.wav")
```

---

## `plot_waveform(audio, fs=44100)`

Displays the waveform using Matplotlib.

### Parameters

| Parameter | Type            |
| --------- | --------------- |
| `audio`   | `numpy.ndarray` |
| `fs`      | `int`           |

### Returns

None

### Example

```python
from pymorsed.audio_encoder import *

audio = morse_to_audio("... --- ...")
plot_waveform(audio)
```

---

# Audio Decoder Module

```python
from pymorsed.audio_decoder import decode_from_file
```

---

## `decode_from_file(filepath)`

Decodes Morse code from a WAV audio file.

The decoder performs:

1. Audio loading
2. Stereo-to-mono conversion
3. Silence trimming
4. Envelope extraction
5. Signal smoothing
6. Thresholding
7. Morse symbol reconstruction
8. Text decoding

### Parameters

| Parameter  | Type  | Description      |
| ---------- | ----- | ---------------- |
| `filepath` | `str` | Path to WAV file |

### Returns

```python
str
```

Decoded text.

### Example

```python
from pymorsed.audio_decoder import decode_from_file

text = decode_from_file("sos.wav")
print(text)
```

Output:

```text
SOS
```

### Exceptions

May raise:

```python
FileNotFoundError
```

If the audio file does not exist.

```python
RuntimeError
```

If decoding fails due to invalid audio data.

---

# Utilities Module

```python
from pymorsed.utils import load_language
```

---

## `load_language(language)`

Loads a language mapping file.

### Parameters

| Parameter  | Type  |
| ---------- | ----- |
| `language` | `str` |

### Returns

```python
dict
```

Dictionary containing character-to-Morse mappings.

### Example

```python
from pymorsed.utils import load_language

mapping = load_language("english")

print(mapping["A"])
```

Output:

```text
.-
```

---

# Top-Level Imports

The package exposes commonly used functions directly from the root package.

```python
from pymorsed import encode
from pymorsed import decode
from pymorsed import morse_to_audio
```

### Example

```python
from pymorsed import encode, decode

morse = encode("HELLO")
text = decode(morse)

print(morse)
print(text)
```

Output:

```text
.... . .-.. .-.. ---
HELLO
```

---

# Supported Languages

Current language mappings:

| Language | Code      |
| -------- | --------- |
| English  | `english` |
| Russian  | `russian` |

Additional language mappings may be added in future releases.
