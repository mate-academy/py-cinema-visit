from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: List[Dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]
    hall = CinemaHall(hall_number)
    cleaner_stuff = Cleaner(cleaner)
    [CinemaBar().sell_product(client.food, client)
     for client in clients]
    hall.movie_session(movie, clients, cleaner_stuff)
