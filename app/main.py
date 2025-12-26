from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers = [Customer(person["name"], person["food"])
                 for person in customers]
    cleaner_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for person in customers:
        CinemaBar.sell_product(person, person.food)

    cinema_hall.movie_session(movie, customers, cleaner_staff)
