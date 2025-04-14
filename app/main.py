from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customers, cleaning_staff)
