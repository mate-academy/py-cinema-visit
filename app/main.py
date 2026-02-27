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
    customer_objects: list[Customer] = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        customer_objects.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, cleaner_obj)
