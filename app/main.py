from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    clients = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    for client in clients:
        cinema_bar.sell_product(client.food, client)

    cleaner_staff = Cleaner(cleaner)
    cinema_hall.movie_session(movie=movie,
                              customers=clients,
                              cleaning_staff=cleaner_staff)
