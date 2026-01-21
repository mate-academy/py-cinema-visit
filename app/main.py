from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str,
) -> None:

    customer_objects = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers
    ]

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    for customer in customer_objects:
        cinema_bar.sell_product(
            customer=customer,
            product=customer.food)

    cinema_hall.movie_session(movie_name, customer_objects, cleaner)
