from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    hall = CinemaHall(hall_number)

    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))
        CinemaBar.sell_product(customers_list[-1], customer["food"])

    hall.movie_session(movie, customers_list, Cleaner(cleaner))
