import re

def refine_prompt(text: str) -> str:
    """Return a cleaned-up version of the user's text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Normalize whitespace
    refined = re.sub(r"\s+", " ", text.strip())

    # Ensure sentence ends with punctuation for clarity
    if refined and refined[-1] not in ".?!":
        refined += "."

    return refined
