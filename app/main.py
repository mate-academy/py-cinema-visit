from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    list_of_customers = [Customer(name=cus["name"], food=cus["food"])
                         for cus in customers]
    for cust in list_of_customers:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    cleaner_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, list_of_customers, cleaner_staff)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number,
             cleaner=cleaner_name, movie=movie)
