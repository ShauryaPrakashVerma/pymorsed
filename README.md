```text
                                                      _ 
                                                     | |
 _ __   _   _  _ __ ___    ___   _ __  ___   ___   __| |
| '_ \ | | | || '_ ` _ \  / _ \ | '__|/ __| / _ \ / _` |
| |_) || |_| || | | | | || (_) || |   \__ \|  __/| (_| |
| .__/  \__, ||_| |_| |_| \___/ |_|   |___/ \___| \__,_|
| |      __/ |                                          
|_|     |___/


```

A Python library for Morse code processing, supporting text encoding/decoding, multi-language mappings, audio signal generation and decoding, and waveform visualization.

<p align="left">
  <a href="https://pypi.org/project/pymorsed/">PyPI</a> •
  <a href="https://shauryaprakashverma.github.io/pymorsed/">Documentation</a>
</p>


<p align="left">
  <a href="https://pepy.tech/projects/pymorsed">
    <img src="https://static.pepy.tech/personalized-badge/pymorsed?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads" alt="PyPI Downloads">
  </a>
  <a href="https://badge.fury.io/py/pymorsed">
    <img src="https://badge.fury.io/py/pymorsed.svg" alt="PyPI version" height="20">
  </a>
</p>


---

## Features

- Convert text to Morse code
- Convert Morse code to text
- Multi-language support
  - English
  - Russian
  - Hindi
- Generate Morse code audio signals
- Decode Morse code from WAV audio files
- Visualize Morse code waveforms
- JSON-based language mappings
- Command-Line Interface (CLI)
- Fully tested with automated CI pipeline

---

## Quick Start

Get started with the most commonly used features:

- [Encode text to Morse code](#encode-text)
- [Decode Morse code to text](#decode-morse-code)
- [Generate Morse audio](#generate-morse-audio)
- [Save Morse audio to a file](#save-audio-to-file)
- [Decode a Morse audio file](#decode-audio-file)
- [Use the Command-Line Interface (CLI)](#command-line-interface-cli)

---

## Installation

```bash
pip install pymorsed
```

---

## Quick Start Examples

### Encode Text

Convert text into Morse code:

```python
from pymorsed import encode

morse = encode("HELLO WORLD")

print(morse)
```

Output:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### Decode Morse Code

Convert Morse code into text:

```python
from pymorsed import decode

text = decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

print(text)
```

Output:

```text
HELLO WORLD
```

### Generate Morse Audio

Generate and play a Morse code audio signal:

```python
from pymorsed import encode
from pymorsed.audio_encoder import morse_to_audio, play_audio

morse = encode("SOS")
audio = morse_to_audio(morse)

play_audio(audio)
```

### Save Audio to File

Save a generated Morse code audio signal:

```python
from pymorsed.audio_encoder import morse_to_audio, save_audio

audio = morse_to_audio("... --- ...")

save_audio(
    audio,
    "sos.wav",
    44100
)
```

### Decode Audio File

Decode Morse code from a WAV audio file:

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

## Command-Line Interface (CLI)

`pymorsed` also provides a command-line interface for performing common Morse
code and audio operations directly from the terminal.

### Available Commands

```text
pymorsed
├── encode
├── decode
├── encode-audio
├── decode-audio
└── version
```

### CLI Examples

Encode text into Morse code:

```bash
pymorsed encode "HELLO WORLD"
```

Decode Morse code into text:

```bash
pymorsed decode ".... . .-.. .-.. ---"
```

Generate and play Morse code audio:

```bash
pymorsed encode-audio "SOS"
```

Save generated audio to a file:

```bash
pymorsed encode-audio "SOS" -o sos
```

The output filename extension is optional. If no extension is provided,
`.wav` is used by default.

Decode a Morse code audio file:

```bash
pymorsed decode-audio "E://audios/sos.wav"
```

Display the available commands:

```bash
pymorsed --help
```

Display the installed version:

```bash
pymorsed --version
```

or:

```bash
pymorsed version
```

For the complete CLI reference, see the
[pymorsed CLI Documentation](https://shauryaprakashverma.github.io/pymorsed/).

---

## Morse Code Conventions

`pymorsed` follows standard Morse code formatting:

| Symbol | Meaning |
| ------ | ------- |
| `.` | Dot |
| `-` | Dash |
| Space (` `) | Letter separator |
| `/` | Word separator |

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

| Language | Code |
| -------- | ---- |
| English | `english` |
| Russian | `russian` |
| Hindi | `hindi` |

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

---

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

---

# License

This project is licensed under the MIT License.

See the LICENSE file for details.
