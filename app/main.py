from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_objs = [Customer(c["name"], c["food"]) for c in customers]

    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for person in customers_objs:
        cinema_bar.sell_product(person.food, person)

    hall.movie_session(movie, customers_objs, cleaner)
