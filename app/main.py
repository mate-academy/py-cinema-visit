from typing import List
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = [Customer(name=c["name"],
                                   food=c["food"]) for c in customers]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie_name=movie, customers=customer_instances,
                              cleaning_staff=cleaner_instance)
