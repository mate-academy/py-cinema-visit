from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_staff = Cleaner(cleaner)

    visitors = [Customer(customer["name"], customer["food"])
                for customer in customers]

    for people in visitors:
        cinema_bar.sell_product(people.food, people)

    cinema_hall.movie_session(movie, visitors, cinema_staff)
