from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def create_customer_instances(customers_data: List[Dict[str, str]])\
        -> List[Customer]:
    return [Customer(name=data["name"],
                     food=data["food"]) for data in customers_data]


def serve_customers(customers: List[Customer]) -> None:
    for customer in customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int, cleaner: str, movie: str) -> None:
    prepared_customers = create_customer_instances(customers)
    serve_customers(prepared_customers)

    cleaning_staff = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(hall_number=hall_number)
    cinema_hall.movie_session(movie_name=movie,
                              customers=prepared_customers,
                              cleaning_staff=cleaning_staff)
