from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    hall = CinemaHall(number=hall_number)

    cleaner_name = Cleaner(name=cleaner)

    cinema_bar = CinemaBar()

    for customer in customers:
        cinema_bar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall.movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaner_name
    )
