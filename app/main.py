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
    cinema_hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)

    for customer in customers:
        current_customer = Customer(customer["name"], customer["food"])

        CinemaBar.sell_product(current_customer, customer["food"])
        customers_list.append(current_customer)

    cinema_hall.movie_session(movie, customers_list, hall_cleaner)
