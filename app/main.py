from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    cleaning_person = Cleaner(cleaner)
    cinema = CinemaHall(hall_number)
    customers_instances = [Customer(customer["name"],
                                    customer["food"])
                           for customer in customers]
    for customer in customers_instances:
        CinemaBar.sell_product(customer, customer.food)
    cinema.movie_session(movie, customers_instances, cleaning_person)
