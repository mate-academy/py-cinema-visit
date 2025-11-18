import datetime
import time as t
from random import randint
from math import ceil, floor


def print_current_time() -> None:
    print(t.time())


def generate_random_tuple(size: int) -> tuple:
    return (randint(-10, 10) for _ in range(size))


def floor_division(value_a: int, value_b: int) -> int:
    return floor(value_a / value_b)


def ceil_division(value_a: int, value_b: int) -> int:
    return ceil(value_a / value_b)


def create_today_date() -> datetime:
    return datetime.date.today()
