from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list = [
        Customer(c["name"], c["food"]) for c in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_list, cleaner_instance)
