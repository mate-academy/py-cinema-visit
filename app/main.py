from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class Distance:
    def __init__(self, value: int | float) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} m"

    def __repr__(self) -> str:
        return f"Distance({self.value})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.value + other.value)
        elif isinstance(other, (int, float)):
            return Distance(self.value + other)
        return NotImplemented

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.value += other.value
        elif isinstance(other, (int, float)):
            self.value += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.value * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.value / other)
        return NotImplemented

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == other
        return False

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < other
        return False

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.value > other.value
        elif isinstance(other, (int, float)):
            return self.value > other
        return False

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.value <= other.value
        elif isinstance(other, (int, float)):
            return self.value <= other
        return False

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.value >= other.value
        elif isinstance(other, (int, float)):
            return self.value >= other
        return False

    def round(self, number: int) -> Distance:
        return Distance(round(self.value, number))


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    # Create Customer instances
    customer_instances = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        customer_instances.append(customer)

    # Sell products in cinema bar
    for customer in customer_instances:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    # Create CinemaHall and Cleaner instances
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    # Start movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
