from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_list = []
    for customer in customers:
        temp = Customer(name=customer["name"], food=customer["food"])
        customer_list.append(temp)
        CinemaBar().sell_product(temp, temp.food)
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_list, cinema_cleaner)
