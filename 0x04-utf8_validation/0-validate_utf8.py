#!/usr/bin/python3
"""utf-8 validator"""


def validUTF8(data) -> bool:
    """."""
    try:
        bytes(data).decode('utf-8')
        return True
    except Exception:
        return False
