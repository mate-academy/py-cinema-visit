from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)

    cleaning_staff = Cleaner(cleaner)

    customer_instances = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]

    for customer_instance in customer_instances:
        CinemaBar.sell_product(
            customer_instance,
            customer_instance.food
        )

    cinema_hall.movie_session(
        movie,
        customer_instances,
        cleaning_staff
    )
