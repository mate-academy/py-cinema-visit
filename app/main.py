from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str,
) -> None:
    customer_instances = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"],
        )

        customer_instances.append(customer_instance)

        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance,
        )

    cleaner_instance = Cleaner(
        name=cleaner,
    )

    cinema_hall = CinemaHall(
        hall_number=hall_number,
    )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance,
    )