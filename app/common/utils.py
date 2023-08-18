import random


def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)


def generate_random_range(max_value: int):
    start = random.randint(0, max_value - 1)
    end = random.randint(start + 1, max_value)
    return start, end
