from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(number=hall_number)
    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner)

    for customer in customer_objects:
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_objects, cleaner)
