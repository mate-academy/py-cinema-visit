from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    new_customers = list[Customer]()
    clean = Cleaner(cleaner)
    cinema = CinemaHall(hall_number)
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(new_customer.food, new_customer)
        new_customers.append(new_customer)
    cinema.movie_session(movie, new_customers, clean)
