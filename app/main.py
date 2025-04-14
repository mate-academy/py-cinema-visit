from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cleaning_staff = Cleaner(cleaner)
    numberhall = CinemaHall(hall_number)
    listcustomers = []
    for i in range(len(customers)):
        listcustomers.append(
            Customer(customers[i]["name"], customers[i]["food"]))
        CinemaBar.sell_product(listcustomers[i], listcustomers[i].food)
    numberhall.movie_session(movie, listcustomers, cleaning_staff)
