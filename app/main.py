from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_registered = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(new_customer, new_customer.food)
        customer_registered.append(new_customer)
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_registered, staff)
