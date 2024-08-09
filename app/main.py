from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    people = []
    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        people.append(person)
        CinemaBar.sell_product(person, person.food)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, people, Cleaner(cleaner))
