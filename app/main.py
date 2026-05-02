from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objects = []
    for data in customers:
        customer = Customer(data["name"], data["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_objects.append(customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, cleaner_obj)
