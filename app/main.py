from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    clients = [
        Customer(client["name"], client["food"]) for client in customers
    ]
    cleaning_staff = Cleaner(cleaner)
    hall1 = CinemaHall(hall_number)
    for client in clients:
        CinemaBar.sell_product(client.food, client)
    hall1.movie_session(movie, clients, cleaning_staff)
