import datetime
import time as t
from random import randint
from math import ceil, floor


def print_current_time() -> None:
    print(t.time())


def generate_random_tuple(size: int) -> tuple:
    return (randint(-10, 10) for _ in range(size))


def floor_division(a: int, b: int) -> int:
    return floor(a / b)


def ceil_division(a: int, b: int) -> int:
    return ceil(a / b)


def create_today_date() -> datetime:
    return datetime.date.today()

