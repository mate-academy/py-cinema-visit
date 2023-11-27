from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    clients = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    bar = CinemaBar()
    staff = Cleaner(cleaner)
    hall_num = CinemaHall(hall_number)

    for client in clients:
        bar.sell_product(client, client.food)

    hall_num.movie_session(movie, clients, staff)
