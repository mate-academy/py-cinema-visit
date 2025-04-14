from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_name = Cleaner(cleaner)
    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]

    for client in clients:
        cinema_bar.sell_product(client, client.food)

    hall.movie_session(movie, clients, cleaner_name)
