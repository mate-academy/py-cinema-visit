from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_cinema_bar = CinemaBar()
    cinema_customer = [Customer(i["name"], i["food"]) for i in customers]

    for i in cinema_customer:
        print(cinema_cinema_bar.sell_product(i.food, i.name))
    return cinema_cinema_hall.movie_session(movie, cinema_customer, cinema_cleaner)
