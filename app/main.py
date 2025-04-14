from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_customers = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        ) for customer in customers
    ]

    for cinema_customer in cinema_customers:
        CinemaBar.sell_product(cinema_customer, cinema_customer.food)

    cinema_cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=cinema_customers,
        cleaning_staff=cinema_cleaner
    )
