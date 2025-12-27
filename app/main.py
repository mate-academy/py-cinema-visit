from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customer_objects = [Customer(name=c["name"], food=c["food"]) for c in customers]
    for customer in customer_objects:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, customer_objects, cleaner)
