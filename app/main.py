from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers_list: list,
    hall_number: int,
    cleaner_name: str,
    movie_name: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)
    customers = [Customer(c["name"], c["food"]) for c in customers_list]

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    hall.movie_session(movie_name, customers, cleaner)

