from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:

    cus = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer["food"], customer_obj)
        cus.append(customer_obj)

    hall_obj = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall_obj.movie_session(movie, cus, cleaner_obj)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.