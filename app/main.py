from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str) -> None:
    for customer_item in customers:
        CinemaBar.sell_product(
            customer_item["food"],
            Customer(customer_item["name"], customer_item["food"])
        )
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie, [Customer(customer_item["name"], customer_item["food"])
                for customer_item in customers], Cleaner(cleaner)
    )
