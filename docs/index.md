
# pymorsed

Python library for encoding, decoding, generating, and analyzing Morse code audio signals.


## Features

- Text to Morse conversion
- Morse to Text conversion
- Multi-language support
- Morse Audio Signal generation 
- Morse Audio Signal decoding from file
- Waveform visualization


## Supported Languages

| Language | Code |
|----------|------|
| English | `english` |
| Russian | `russian` |

Example:

```python
from pymorsed.utils import load_language

mapping = load_language("russian")
```

!!! tip

    Additional language mappings will be added in future releases.

## License
pymorsed is released under the MIT License.
See the LICENSE file for full details.