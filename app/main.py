from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances = []

    for customer_data in customers:
        customer_instances.append(
            Customer(
                customer_data["name"],
                customer_data["food"]
            )
        )

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    hall.movie_session(movie, customer_instances, cleaner_name)
