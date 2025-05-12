from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[dict], hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:
    customer_list = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaning_staff)
    for customer in customer_list:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.watch_movie(movie_name=movie_name,
                              customers=customer_list,
                              cleaning_staff=cleaner)
