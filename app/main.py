from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customer_instances = [Customer(c["name"], c["food"]) for c in customers]

    for customer in customer_instances:
        cb.sell_product(customer=customer,
                        product=customer.food)

    ch.movie_session(movie_name=movie,
                     customers=customer_instances,
                     cleaning_staff=cleaning_staff)
customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")