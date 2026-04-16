from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str) -> None:

    cinema_hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    customer_objects = []

    for customer in customers:
        customer_objects.append(
            Customer(customer["name"], customer["food"])
        )

    for cust in customer_objects:
        CinemaBar.sell_product(customer=cust, product=cust.food)

    cinema_hall.movie_session(movie, customer_objects, staff)
