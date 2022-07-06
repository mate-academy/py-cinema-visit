from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    client_list = []
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)

    for client in customers:
        customer = Customer(client["name"], client["food"])
        client_list.append(customer)
        CinemaBar.sell_product(client["food"], customer)
    CinemaHall.movie_session(hall_number, movie, client_list, cleaner)
