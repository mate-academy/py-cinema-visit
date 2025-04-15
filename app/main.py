from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_customers = [Customer(customer["name"], customer["food"])
                        for customer in customers]

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in cinema_customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie_name=movie,
                              customers=cinema_customers,
                              cleaning_staff=cleaner)
