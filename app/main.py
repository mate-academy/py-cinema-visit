from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_obj = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(
        hall_number
    )
    cleaner = Cleaner(cleaner)
    for obj in customers_obj:
        cinema_bar.sell_product(obj.food, obj)
    cinema_hall.movie_session(
        movie, customers_obj, cleaner
    )
