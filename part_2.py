import random
from typing import List


def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:

    if (
        min < 1
        or max > 1000
        or min > max
        or quantity < 0
        or quantity > (max - min + 1)
    ):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)


if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6))
