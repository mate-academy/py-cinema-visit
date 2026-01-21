# write your imports here
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    clients = []

    for customer in customers:
        client = Customer(customer["name"], customer["food"])
        clients.append(client)
        cinema_bar.sell_product(client, customer["food"])

    cinema_hall.movie_session(movie, clients, cleaning_staff)
