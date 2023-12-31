#!/usr/bin/python3
"""utf-8 validator module."""

from typing import Tuple, List


def validUTF8(data):
    """Check if bytes list is a valid utf-8.
    Args:
    data: list of bytes that is suppose to be unicode
    Returns: True or false
    """
    _cont = 0
    n_byte = 0
    for _byte in data:
        if not n_byte:
            if _byte > 255:
                _byte = _byte & 255
            n_byte, _c = bom_or_cont(_byte)
            if _c:
                return False
        else:
            _, _cont = bom_or_cont(_byte)
            if n_byte and _cont:
                n_byte -= 1
            elif n_byte and not _cont:
                return False
    if n_byte:
        return False
    return True


def bom_or_cont(_byte) -> Tuple[int, int]:
    """Check if it a byte order.
    Args:
    byte: the byte to check
    Return: Tuple of n_byte and cont
    """
    _bom = 0b10000000
    _7bit = 0b01000000
    _6bit = 0b00100000
    _5bit = 0b00010000
    _cont = 0
    n_byte = 0
    if _byte & _bom:
        if _byte & _7bit:
            n_byte += 1
            if _byte & _6bit:
                n_byte += 1
                if _byte & _5bit:
                    n_byte += 1
        else:
            _cont = 1
    return (n_byte, _cont)
