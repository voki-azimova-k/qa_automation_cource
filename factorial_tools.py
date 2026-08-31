import sys
import time
from functools import wraps

sys.setrecursionlimit(5000)


class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        elapsed_time = end_time - self.start_time
        print(f"Execution time: {elapsed_time:.8f} seconds")


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if number in (0, 1):
        return 1

    return number * factorial(number - 1)


def cache_result(function):
    cache = {}

    @wraps(function)
    def wrapper(number):
        if number in cache:
            return cache[number]

        result = function(number)
        cache[number] = result
        return result

    wrapper.cache = cache

    return wrapper


@cache_result
def cached_factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if number in (0, 1):
        return 1

    return number * cached_factorial(number - 1)


def factorial_cache_generator(limit):
    result = 1

    for number in range(limit + 1):
        if number > 1:
            result *= number

        yield number, result


if __name__ == "__main__":
    print("Factorial 100 without cache:")
    with Timer():
        factorial(100)

    print("\nFactorial 1000 without cache:")
    with Timer():
        factorial(1000)

    print("\nFactorial 1000 with empty cache:")
    cached_factorial.cache.clear()

    with Timer():
        cached_factorial(1000)

    print("\nFactorial 1000 repeated with cache:")
    with Timer():
        cached_factorial(1000)

    print("\nFactorial 1000 with preinitialized cache:")
    cached_factorial.cache.clear()

    for number, result in factorial_cache_generator(900):
        cached_factorial.cache[number] = result

    with Timer():
        cached_factorial(1000)
