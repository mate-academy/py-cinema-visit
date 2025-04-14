from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    clients = [
        Customer(person.get("name"),
                 person.get("food")) for person in customers
    ]
    cinema = CinemaHall(hall_number)
    CinemaBar()
    cleaner = Cleaner(cleaner)
    for client in clients:
        CinemaBar.sell_product(client, client.food)
    cinema.movie_session(movie, clients, cleaner)
