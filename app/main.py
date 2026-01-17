from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    result = []

    cleaner_instance = Cleaner(cleaner)

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"],
        )

        CinemaBar.sell_product(
            product=customer["food"],
            customer=customer_instance,
        )

        result.append(customer_instance)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, result, cleaner_instance)
