from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    customer_objects = [
        Customer(info["name"], info["food"])
        for info in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_objects, cinema_cleaner)
