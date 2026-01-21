from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    people = [Customer(custom["name"], custom["food"]) for custom in customers]
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    for man in people:
        bar.sell_product(man.food, man)
    hall.movie_session(movie, people, clean)
