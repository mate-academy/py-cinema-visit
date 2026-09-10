from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 number: int,
                 cleaner: str,
                 movie: str) -> None:

    all_customers = [Customer(customer["name"],
                              customer["food"]) for customer in customers]
    cinema_hall = CinemaHall(number)
    cleaning_staff = Cleaner(cleaner)
    for customer in all_customers:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, all_customers, cleaning_staff)
