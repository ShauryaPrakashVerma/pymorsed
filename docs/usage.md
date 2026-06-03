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
## Morse Code Spacing Rules

pymorsed follows standard Morse code spacing conventions when encoding and decoding messages.

### Letter Separation

Individual Morse symbols within a letter are written together without spaces.

Examples:

| Character | Morse Code |
| --------- | ---------- |
| A         | `.-`       |
| B         | `-...`     |
| S         | `...`      |
| O         | `---`      |

---

### Word Separation

Letters are separated by a single space.

Example:

```text
HELLO
```

becomes:

```text
.... . .-.. .-.. ---
```

Notice that each Morse letter is separated by one space.

---

### Multiple Words

Words are separated using the forward slash character (`/`).

Example:

```text
HELLO WORLD
```

becomes:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

The slash represents a word boundary.

---

### Summary

| Morse Pattern | Meaning           |
| ------------- | ----------------- |
| `.`           | Dot               |
| `-`           | Dash              |
| Space (` `)   | Separates letters |
| Slash (`/`)   | Separates words   |

!!! note

```
When manually providing Morse code to `decode()`, use a single space between letters and a forward slash (`/`) between words.
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

