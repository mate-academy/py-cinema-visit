from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []
    for custom_items in customers:
        next_customer = Customer(custom_items["name"], custom_items["food"])
        list_of_customers.append(next_customer)
    cinema_inst = CinemaHall(hall_number)
    cleaner_it = Cleaner(cleaner)
    for custom_items in list_of_customers:
        cb = CinemaBar()
        cb.sell_product(custom_items.food, custom_items)
    cinema_inst.movie_session(movie, list_of_customers, cleaner_it)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 4
cleaner_name = "Anna"
movie = "I'm Robot"
cinema_visit(customers=customers,
             hall_number=hall_number,
             cleaner=cleaner_name,
             movie=movie)
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.
