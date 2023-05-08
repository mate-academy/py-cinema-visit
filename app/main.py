from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    people = []
    number = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    for person in customers:
        person = Customer(person["name"], person["food"])
        people.append(person)
        CinemaBar.sell_product(person.food, person)

    number.movie_session(movie, people, staff)
