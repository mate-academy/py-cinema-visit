# Cinema
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

# People
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    all_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    hall = CinemaHall(hall_number)

    cleaner = Cleaner(cleaner)

    for customer in all_customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(
        movie_name=movie,
        customers=all_customers,
        cleaning_staff=cleaner
    )
