#!/usr/bin/python3
"""Lock Box."""


def canUnlockAll(boxes):
    """Check if all in a lock box can be unlocked."""
    length = len(boxes)
    unlock_box = set([0])
    for idx_b, box in enumerate(boxes):
        for idx in box:
            if idx_b == idx:
                continue
            if idx >= length:
                return False
            unlock_box.add(idx)
    return len(unlock_box) == length
