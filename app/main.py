from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_list = [Customer(client["name"], client["food"])
                     for client in customers]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_ = Cleaner(cleaner)

    for client in customer_list:
        cinema_bar.sell_product(client.food, client)

    cinema_hall.movie_session(movie, customer_list, cleaner_)
