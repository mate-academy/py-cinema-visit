from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    bar_object = CinemaBar()

    customer_objects = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)

    for customer in customer_objects:
        bar_object.sell_product(customer, customer.food)

    hall.movie_session(movie, customer_objects, cleaner_name)
