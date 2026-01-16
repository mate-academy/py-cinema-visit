from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str,
) -> None:
    if (
        isinstance(movie, list)
        and isinstance(customers, int)
        and isinstance(hall_number, str)
    ):
        movie_var = cleaner
        customers_var = movie
        hall_number_var = customers
        cleaner_var = hall_number

    customers_list = []
    for customer in customers_var:
        new_customer = Customer(customer["name"], customer["food"])
        customers_list.append(new_customer)
        CinemaBar.sell_product(customer["food"], new_customer)
    cinema_hall = CinemaHall(hall_number_var)
    clean_staff = Cleaner(cleaner_var)
    cinema_hall.movie_session(movie_var, customers_list, clean_staff)
