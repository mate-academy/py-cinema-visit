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
    customer_list = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customer_list.append(customer)
        CinemaBar().sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    clean_staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, clean_staff)
