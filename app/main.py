from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning = Cleaner(cleaner)

    for customer in customers:
        customer_result = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        cinema_bar.sell_product(
            customer=customer_result,
            product=customer_result.food
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer(**kwargs) for kwargs in customers],
        cleaning_staff=cleaning
    )
