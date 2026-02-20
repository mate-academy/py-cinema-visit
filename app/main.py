from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str) -> None:
    cleaner_instance = Cleaner(name=cleaner)

    customer_instances = []

    for customer_data in customers:
        customer_instance = Customer(
            name=customer_data["name"],
            food=customer_data["food"],
        )
        customer_instances.append(customer_instance)

        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance,
        )

    hall_instance = CinemaHall(hall_number=hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance,
    )