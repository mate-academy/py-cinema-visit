from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    shop = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaning = Cleaner(cleaner)
    visitors = [
        Customer(client["name"], client["food"])
        for client in customers
    ]
    for client in visitors:
        shop.sell_product(client.food, client)
    hall.movie_session(movie, visitors, cleaning)
