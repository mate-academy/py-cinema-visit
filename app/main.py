from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str,
) -> None:
    customers_elem = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    hall_numb = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    cinema_bar = CinemaBar()

    for consumer in customers_elem:
        cinema_bar.sell_product(consumer.food, consumer)
    hall_numb.movie_session(movie_name, customers_elem, cleaner)
