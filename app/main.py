from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances = [Customer(customer["name"], customer["food"])
                           for customer in customers]

    for customer in customers_instances:
        CinemaBar.sell_product(customer.food, customer)

    cleaner_instance = Cleaner(cleaner)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_instances, cleaner_instance)
