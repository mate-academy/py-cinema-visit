from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cust_list = [Customer(cust["name"], cust["food"]) for cust in customers]

    for cust in cust_list:
        CinemaBar.sell_product(cust, cust.food)

    the_cleaner = Cleaner(cleaner)

    hall = CinemaHall(hall_number)



    hall.movie_session(movie, cust_list, the_cleaner)

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)

