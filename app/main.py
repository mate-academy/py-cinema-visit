from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    peoples = [
        Customer(people["name"], people["food"])
        for people in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cleaning = Cleaner(cleaner)

    for people in peoples:
        CinemaBar.sell_product(people, people.food)

    cinema_hall.movie_session(movie, peoples, cleaning)
