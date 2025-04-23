from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    for customer in customers:
        print(f"Cinema bar sold {customer['food']} to {customer['name']}.")

    print(f"\"{movie}\" started in hall number {hall_number}.")
    for customer in customers:
        print(f"{customer['name']} is watching \"{movie}\".")
    print(f"\"{movie}\" ended.")
    print(f"Cleaner {cleaner} is cleaning hall number {hall_number}.")
