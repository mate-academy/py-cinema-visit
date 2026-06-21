# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    persons = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_staff = Cleaner(cleaner)
    for person in persons:
        cinema_bar.sell_product(person.food, person)
    cinema_hall.movie_session(movie, persons, cinema_staff)
