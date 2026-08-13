from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers = [
        Customer(**customer) for customer in customers
    ]
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(movie=movie,
                       customers=customers,
                       cleaning_staff=cleaning_staff)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
