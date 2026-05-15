# write your imports here
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
    customer_objects = [
        Customer(c["name"], c["food"])
        for c in customers
    ]

    for c_obj in customer_objects:
        CinemaBar.sell_product(c_obj.food, c_obj)

    cleaner_obj = Cleaner(cleaner)
    hall_obj = CinemaHall(hall_number)

    hall_obj.movie_session(movie, customer_objects, cleaner_obj)
