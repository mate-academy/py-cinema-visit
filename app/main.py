from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    num_halls = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    cinema_guest = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        cinema_guest.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall.movie_session(num_halls, movie, cinema_guest, cleaner_name)
