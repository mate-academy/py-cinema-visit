from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    list_of_customers = [Customer(name=customer["name"], food=customer["food"])
                         for customer in customers]
    for customer in list_of_customers:
        CinemaBar.sell_product(customer.food, customer)

    CinemaHall.movie_session(CinemaHall(hall_number),
                             movie_name=movie,
                             customers=list_of_customers,
                             cleaning_staff=Cleaner(cleaner))
