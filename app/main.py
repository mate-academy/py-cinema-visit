from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    object_cinema_hall = CinemaHall(hall_number)
    object_cleaner = Cleaner(cleaner)
    object_customers = [
        Customer(man["name"], man["food"])
        for man in customers
    ]
    for obj in object_customers:
        CinemaBar.sell_product(obj, obj.food)

    object_cinema_hall.movie_session(movie, object_customers, object_cleaner)
