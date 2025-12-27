from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    people = []
    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(person.food, person)
        people.append(person)
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    hall.movie_session(movie, people, staff)
