from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objects = []

    for customer in customers:
        customer_object = Customer(
            name=customer["name"],
            food=customer["food"],
        )

        customer_objects.append(customer_object)

        CinemaBar.sell_product(
            product=customer_object.food,
            customer=customer_object,
        )

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff,
    )
