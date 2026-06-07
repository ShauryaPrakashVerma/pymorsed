# pymorsed

A Python library for encoding, decoding, generating, and analyzing Morse code audio signals.

📦 PyPI: https://pypi.org/project/pymorsed/

📖 Documentation: https://shauryaprakashverma.github.io/pymorsed/

## Features

* Convert text to Morse code
* Convert Morse code to text
* Multi-language support

  * English
  * Russian
* Generate Morse code audio signals
* Decode Morse code from WAV audio files
* Visualize Morse code waveforms
* JSON-based language mappings
* Fully tested with automated CI pipeline



<br>

## Installation

```bash
pip install pymorsed
```

---

## Quick Start

### Encode Text

```python
from pymorsed import encode

morse = encode("HELLO WORLD")
print(morse)
```

Output:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

---

### Decode Morse Code

```python
from pymorsed import decode

text = decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
print(text)
```

Output:

```text
HELLO WORLD
```

---

### Generate Morse Audio

```python
from pymorsed import encode
from pymorsed.audio_encoder import morse_to_audio

morse = encode("SOS")
audio = morse_to_audio(morse)
play_audio(audio)
```

---

### Save Audio to File

```python
from pymorsed.audio_encoder import (
    morse_to_audio,
    save_audio
)

audio = morse_to_audio("... --- ...")

save_audio(
    audio,
    "sos.wav",
    44100
)
```

---

### Decode Audio File

```python
from pymorsed.audio_decoder import decode_from_file

text = decode_from_file("sos.wav")

print(text)
```

Output:

```text
SOS
```

---

## Morse Code Conventions

pymorsed follows standard Morse code formatting:

| Symbol      | Meaning          |
| ----------- | ---------------- |
| `.`         | Dot              |
| `-`         | Dash             |
| Space (` `) | Letter separator |
| `/`         | Word separator   |

Example:

```text
HELLO WORLD
```

becomes:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

---

## Supported Languages

| Language | Code      |
| -------- | --------- |
| English  | `english` |
| Russian  | `russian` |

Additional language mappings may be added in future releases.

---

## Example Imports

### Root Package Imports

```python
from pymorsed import encode
from pymorsed import decode
```

### Module Imports

```python
from pymorsed.encoder import encode
from pymorsed.decoder import decode

from pymorsed.audio_encoder import (
    morse_to_audio,
    play_audio,
    save_audio,
    plot_waveform
)

from pymorsed.audio_decoder import decode_from_file
```

<br>


# Development

Clone the repository:

```bash
git clone https://github.com/ShauryaPrakashVerma/pymorsed.git
cd pymorsed
```

Install dependencies:

```bash
pip install -e .
```

Run tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=pymorsed
```

<br>

# License

This project is licensed under the MIT License.

See the LICENSE file for details.

<br>

