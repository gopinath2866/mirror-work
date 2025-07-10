# divine_number.py

import hashlib

def divine_number_from_input(text: str) -> int:
    """
    Turns user input into a symbolic number between 1 and 9.
    Uses hash-based spiral mapping to simulate energetic resonance.
    """
    if not text.strip():
        return 9  # Default to embrace when no input

    # Hash the text to create repeatable, symbolic energy
    hash_digest = hashlib.md5(text.encode('utf-8')).hexdigest()
    numeric_value = sum(int(char, 16) for char in hash_digest if char.isdigit())

    # Spiral logic (1–9)
    return (numeric_value % 9) + 1
