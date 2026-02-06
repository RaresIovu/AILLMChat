import re
import unicodedata
SUPERSCRIPTS = str.maketrans(
    "0123456789-",
    "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"
)
SUBSCRIPTS = str.maketrans(
    "0123456789-",
    "₀₁₂₃₄₅₆₇₈₉₋"
)

def normalize_ro_diacritics(text: str) -> str:
    if not text:
        return text
    return (text
            .replace("ş", "ș").replace("Ş", "Ș")
            .replace("ţ", "ț").replace("Ţ", "Ț"))

def replace_powers(text: str) -> str:
    def repl(match):
        number = match.group(1)
        return number.translate(SUPERSCRIPTS)
    
    return re.sub(r"\^(-?\d+)", repl, text)

def replace_indices(text: str) -> str:
    def repl(match):
        number = match.group(1)
        return number.translate(SUBSCRIPTS)
    return re.sub(r"\_(-?\d+)", repl, text)

def format_text(text: str) -> str:
    if not text:
        return text
    text = unicodedata.normalize("NFKC", text)
    text = replace_powers(text)
    text = replace_indices(text)
    text = normalize_ro_diacritics(text)
    text = text.replace(". ", "\n")
    return text