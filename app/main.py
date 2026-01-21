from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_instance = []
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(new_customer, new_customer.food)
        customers_instance.append(new_customer)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_instance, cleaner)
