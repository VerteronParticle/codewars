"""Return numeric value of all characters in text."""


def alphabet_position(text):
    """Return numeric value, account for offset."""
    return ' '.join(
        str(ord(c) - 96) for c in text.lower() if c.isalpha()
    )
