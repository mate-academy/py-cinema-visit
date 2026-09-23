from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    result_list = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(cust, customer["food"])
        result_list.append(cust)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_hall.movie_session(movie, result_list, cleaning_staff)
