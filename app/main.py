from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objects = [
        Customer(
            name=customer["name"],
            food=customer["food"],
        )
        for customer in customers
    ]

    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food,
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner,
    )
