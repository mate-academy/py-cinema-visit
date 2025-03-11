# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    clients = []
    room = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    for i in customers:
        customer = Customer(i["name"], i["food"])
        clients.append(customer)
        CinemaBar.sell_product(i["food"], customer)

    room.movie_session(movie, clients, staff)
