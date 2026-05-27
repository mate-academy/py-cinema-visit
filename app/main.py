from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers = [Customer(name=customer["name"],
                          food=customer["food"]) for customer in customers]
    cleaner = Cleaner(cleaner)
    cinema = CinemaHall(hall_number)
    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)
    cinema.movie_session(movie, customers, cleaner)
