from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    clients = [
        Customer(client["name"], client["food"])
        for client in customers
    ]
    hall = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)

    for client in clients:
        CinemaBar.sell_product(client, client.food)

    hall.movie_session(movie, clients, cleaner_person)
