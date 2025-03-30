from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner_name: str,
    movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hull = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    customers_list = []

    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer, customer.food)

    cinema_hull.movie_session(movie, customers_list, cleaner)
