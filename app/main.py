from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    clients = []
    for person in customers:
        clients.append(Customer(person["name"], person["food"]))
    for client in clients:
        CinemaBar.sell_product(client.food, client)

    cleaner_staff = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie=movie,
                                          customers=clients,
                                          cleaning_staff=cleaner_staff)
