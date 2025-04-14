from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances = [Customer(**person) for person in customers]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for person in customers_instances:
        CinemaBar.sell_product(person.food, person)

    hall.movie_session(movie, customers_instances, cleaner)
