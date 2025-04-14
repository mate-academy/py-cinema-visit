from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    people = []
    for person in customers:
        people.append(Customer(person.get("name"), person.get("food")))
    cinema_hall = CinemaHall(hall_number)
    CinemaBar()
    first_cleaner = Cleaner(cleaner)
    for person in people:
        CinemaBar.sell_product(person, person.food)
    cinema_hall.movie_session(
        movie,
        people,
        first_cleaner
    )
