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
    movie_info = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)

    for index, customer in enumerate(customers):
        customers_list.append(Customer(customer["name"], customer["food"]))
        CinemaBar.sell_product(customer["food"], customers_list[index])

    movie_info.movie_session(movie, customers_list, hall_cleaner)
