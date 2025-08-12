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
    customer_instances = []

    for customer in customers:
        customer_instances.append(
            Customer(name=customer["name"], food=customer["food"])
        )

    hall = CinemaHall(hall_number)
    cleaning_worker = Cleaner(cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_stuff=cleaning_worker
    )
