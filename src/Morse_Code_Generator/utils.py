import json
from pathlib import Path
from functools import lru_cache


def load_language(language = "english"):
    language = language.lower()
    
    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / f"{language}.json"
    )
    
    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
    
@lru_cache(maxsize=None)
def build_lookup(language = "english"):
    language = language.lower()
    morse_data = load_language(language)
    
    lookup = {}

    for category in ["letters", "numbers", "special_characters"]:
        lookup.update(morse_data.get(category, {}))

    return lookup

@lru_cache(maxsize=None)
def build_reverse_lookup(language = "english"):
    language = language.lower()
    lookup = build_lookup(language)
    return {v:k for k,v in lookup.items()}
# lru cache --->  read, learn about this. Implement it