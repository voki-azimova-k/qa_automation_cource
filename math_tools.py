import math
import random
from collections import Counter
from datetime import datetime

from factorial_tools import factorial, cached_factorial, Timer


def log_with_timestamp(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def random_numbers_distribution(count, low, high):
    numbers = [random.randint(low, high) for _ in range(count)]
    return Counter(numbers)


if __name__ == "__main__":
    number = 1000

    log_with_timestamp(f"Start comparing factorial({number}) implementations")

    print("\nmath.factorial (built-in):")
    with Timer():
        math.factorial(number)

    print("\nfactorial (recursive, own implementation):")
    with Timer():
        factorial(number)

    print("\ncached_factorial (own implementation, empty cache):")
    cached_factorial.cache.clear()
    with Timer():
        cached_factorial(number)

    log_with_timestamp("Finished comparing factorial implementations")

    log_with_timestamp("Start generating random numbers distribution")

    distribution = random_numbers_distribution(count=1000, low=1, high=6)

    print("\nDistribution of 1000 random integers (1-6):")
    for value in sorted(distribution):
        print(f"{value}: {distribution[value]}")

    log_with_timestamp("Finished generating random numbers distribution")
