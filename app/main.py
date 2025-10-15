# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # write you code here
    customs = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for cust in customs:
        CinemaBar().sell_product(cust.food, cust)
    hall.movie_session(movie_name=movie, customers=customs, cleaning_staff=cleaner)


# customers = [
#     {"name": "Bob", "food": "Coca-cola"},
#     {"name": "Alex", "food": "popcorn"}
# ]
# hall_number = 5
# cleaner_name = "Anna"
# movie = "Madagascar"
# cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)
#
#
