from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers = [Customer(person["name"], person["food"])
                 for person in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for person in customers:
        CinemaBar.sell_product(person, person.food)

    cinema_hall.movie_session(movie, customers, cleaning_staff)
