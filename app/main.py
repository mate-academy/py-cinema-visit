from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    cleaner_object = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_object,
    )
