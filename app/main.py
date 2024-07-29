from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    people = [
        Customer(name=person.get("name"), food=person.get("food"))
        for person in customers
    ]
    hall_number = CinemaHall(hall_number)

    for person in people:
        CinemaBar.sell_product(product=person.food, customer=person)

    hall_number.movie_session(movie, people, Cleaner(cleaner))
