from .utils import build_reverse_lookup

def decode(morse_str, language = "english") -> str:
    
    """
    Decode Morse Code to a string.

    Args:
        morse_str (str): The morse code string in the form of dits and dashes.
        language (str): The language of the decoded message.

    Returns:
        str: The english language equivalent of the morse code.
    """
    
    language = language.lower()
    reverse_lookup = build_reverse_lookup(language)
    result = []
    for symbol in morse_str.split():
        if symbol == "/":
            result.append(" ")
        elif symbol in reverse_lookup:
            result.append(reverse_lookup[symbol])
        else:
            raise ValueError(f"Morse '{symbol}' not recognized")

    return "".join(result)
