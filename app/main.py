from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer_instance in customers:
        CinemaBar.sell_product(customer_instance.food, customer_instance)

    cinema_hall.movie_session(movie, customers, cleaner)
