from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    people = []
    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        people.append(person)
        CinemaBar.sell_product(person.food, person)
    cinema_hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    cinema_hall.movie_session(movie, people, staff)
