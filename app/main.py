from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    people = []
    for customer in customers:
        cb = CinemaBar()
        customer_obj = Customer(customer["name"], customer["food"])
        cb.sell_product(customer=customer_obj, product=customer_obj.food)
        people.append(customer_obj)

    cleaner_person = Cleaner(cleaner)
    ch = CinemaHall(hall_number)
    ch.movie_session(movie, people, cleaner_person)
