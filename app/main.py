from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers = [Customer(person["name"], person["food"])
                 for person in customers]

    for person in customers:
        CinemaBar.sell_product(person.food, person)

    cleaner_name = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers, cleaner_name)
