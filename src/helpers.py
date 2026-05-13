import random


def get_data():
    """Get random data from a list."""
    data = ["apple", "banana", "cherry"]
    idx = random.randint(0, len(data) - 1)
    return data[idx]
