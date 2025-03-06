from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from typing import List, Dict


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers]

    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    print(f"\"{movie}\" started in hall number {hall.number}.")
    for customer in customer_objects:
        print(f"{customer.name} is watching \"{movie}\".")

    print(f"\"{movie}\" ended.")
    print(
        f"Cleaner {cleaning_staff.name} "
        f"is cleaning hall number {hall.number}."
    )


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers,
                 hall_number=hall_number,
                 cleaner=cleaner_name,
                 movie=movie)
