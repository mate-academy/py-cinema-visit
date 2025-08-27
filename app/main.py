from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers = [Customer(d["name"], d["food"]) for d in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(
        customers=customers,
        cleaning_staff=cleaner_instance,
        movie_name=movie,
    )


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner = "Anna"
movie = "Madagascar"
cinema_visit(movie=movie, customers=customers,
             hall_number=hall_number, cleaner=cleaner)
