from .utils import build_lookup



def encode(input_msg, language = "english") -> str:
    
    """
    Encode a string into Morse Code

    Args:
        input_msg (str): The text to be converted into Morse Code.
        language (str): The language of the message.

    Returns:
        str: A string of dots and dashes i.e. the morse code of the input string.
    """
    language = language.lower()
    lookup = build_lookup(language)
    
    final_msg = []
    
    for char in input_msg.upper():
        if char in lookup:
            final_msg.append(lookup[char])
        else:
            raise ValueError(f"Character '{char}' not supported.")
    
    return " ".join(final_msg)
        
        

