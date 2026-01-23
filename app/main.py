from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    persons = []
    for customer in customers:
        persons.append(Customer(name=customer["name"], food=customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for person in persons:
        CinemaBar.sell_product(customer=person, product=person.food)
    CinemaHall.movie_session(hall, movie, persons, cleaner)
