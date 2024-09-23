from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        ) for customer in customers
    ]

    for customer in customers_list:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=Cleaner(cleaner)
    )
