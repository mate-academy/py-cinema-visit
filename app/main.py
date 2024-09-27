from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    all_customers = []
    for man in customers:
        all_customers.append(Customer(man["name"], man["food"]))

    hall = CinemaHall(hall_number)
    bar = CinemaBar()

    for man in all_customers:
        bar.sell_product(man, man.food)

    clean_man = Cleaner(cleaner)

    hall.movie_session(movie, all_customers, clean_man)
