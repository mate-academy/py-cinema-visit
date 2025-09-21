# write your imports here
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_objects = []
    for customer in customers:
        name = customer['name']
        food = customer['food']
        _customer = Customer(name, food)
        customers_objects.append(_customer)
        CinemaBar.sell_product(_customer, food)
    hall.movie_session(movie, customers_objects, cleaner)

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)