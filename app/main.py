from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_client = [Customer(client['name'],
                            client["food"])
                   for client in customers]
    cleaner = Cleaner(cleaner)
    cn = CinemaHall(hall_number)
    for client in list_client:
        CinemaBar.sell_product(client, client.food)
    cn.movie_session(movie, list_client, cleaner)
