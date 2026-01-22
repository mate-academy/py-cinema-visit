from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie_name: str
) -> None:

    list_of_customers = [Customer(customer["name"], customer["food"])
                         for customer
                         in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in list_of_customers:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie_name, list_of_customers, cleaner)
