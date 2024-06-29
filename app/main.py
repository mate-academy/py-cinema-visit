from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    customers_as_classes = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cleaner_as_class = Cleaner(cleaner)

    for customer in customers_as_classes:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_as_classes,
                              cleaning_staff=cleaner_as_class)
