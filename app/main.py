from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    visitors = []
    for person in customers:
        visitors.append(Customer(person["name"], person["food"]))
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for person in visitors:
        bar.sell_product(person.food, person)
    hall.movie_session(movie, visitors, cleaner)
