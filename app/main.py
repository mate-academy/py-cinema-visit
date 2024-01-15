from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar
    staff = Cleaner(cleaner)

    list_of_customers = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(customer)
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, list_of_customers, staff)
