from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    list_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cb = CinemaBar()
    for customer in list_customers:
        cb.sell_product(customer=customer, product=customer.food)

    cinema = CinemaHall(hall_number)
    cinema.movie_session(movie, list_customers, Cleaner(cleaner))


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]

hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"

cinema_visit(
    customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar"
)
