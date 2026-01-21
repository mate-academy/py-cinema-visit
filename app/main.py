from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    clients = []
    for person in customers:
        temp = Customer(person["name"], person["food"])
        clients.append(temp)
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    cinema_bar = CinemaBar
    for person in clients:
        cinema_bar.sell_product(person, person.food)
    hall.movie_session(movie, clients, staff)
