from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers, hall_number, cleaner_name, movie)
