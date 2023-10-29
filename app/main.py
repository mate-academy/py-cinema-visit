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

    hall = CinemaHall(hall_number)
    bar_service = CinemaBar
    staff = Cleaner(cleaner)

    list_of_customers = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(customer)
        bar_service.sell_product(customer, customer.food)

    hall.movie_session(movie, list_of_customers, staff)
