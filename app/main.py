from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]
    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for person in customers:
        bar.sell_product(person.food, person)

    hall.movie_session(movie, customers, cleaner)
