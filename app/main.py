from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_cinemahall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_cinemabar = CinemaBar()
    cinema_customer = [Customer(i["name"], i["food"]) for i in customers]

    for i in cinema_customer:
        print(cinema_cinemabar.sell_product(i.food, i.name))
    print(cinema_cinemahall.movie_session(movie, cinema_customer, cinema_cleaner))
    return(cinema_cleaner.clean_hall(hall_number))

customers = [
 {"name": "Bob", "food": "Coca-cola"},
 {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
print(cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie))
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.