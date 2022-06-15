from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    clients = []

    for customer in customers:
        client = Customer(customer['name'], customer['food'])
        clients.append(client)
        CinemaBar.sell_product(client, customer['food'])

    cinema_hall.movie_session(movie, clients, cleaner)
