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
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )

    hall = CinemaHall(number=hall_number)
    cleaner_object = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_object,
    )
