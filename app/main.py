from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = [
        Customer(
            customer.get("name", "NoName"), customer.get("food", "NoFood")
        )
        for customer in customers
    ]

    for customer_obj in customer_objects:
        CinemaBar.sell_product(customer_obj.food, customer_obj)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_objects, Cleaner(cleaner))
