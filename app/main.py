from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    customer_instance = []
    for _ in customers:
        customer = Customer(_["name"], _["food"])
        customer_instance.append(customer)
        CinemaBar.sell_product(_["food"], customer)

    hall_instance.movie_session(movie, customer_instance, cleaner_instance)
