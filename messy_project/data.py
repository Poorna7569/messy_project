import random

def get_data():
    data = ["apple", "banana", "cherry"]
    idx = random.randint(0, len(data) - 1)
    return data[idx]
