from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:

    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    clients = [Customer(
        name=customer["name"],
        food=customer["food"])
        for customer in customers
    ]

    for customer in clients:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(
        movie_name=movie,
        customers=clients,
        cleaning_staff=cleaner)
