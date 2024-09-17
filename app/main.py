from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaning_staff)
    cinema_bar = CinemaBar()
    for client in clients:
        cinema_bar.sell_product(product=client.food, customer=client)
    hall.movie_session(movie_name=movie_name,
                       customers=clients,
                       cleaning_staff=staff)
