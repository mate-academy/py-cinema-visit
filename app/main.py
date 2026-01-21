from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int, cleaner: str, movie: str) -> None:
    customer_objs = [
        Customer(customer["name"], customer["food"]) for customer in customers]
    for customer_obj in customer_objs:
        CinemaBar.sell_product(customer_obj.food, customer_obj)
    CinemaHall(hall_number).movie_session(
        movie, customer_objs, Cleaner(cleaner)
    )


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5,
             cleaner="Anna", movie="Madagascar")
