from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    clients = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(new_customer, new_customer.food)
        clients.append(new_customer)

    cinema_hall.movie_session(movie, clients, cleaning_staff)
