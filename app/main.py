from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    people = []
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)

    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        people.append(person)
        cinema_bar.sell_product(person.food, person)

    cinema_hall.movie_session(movie, people, cinema_cleaner)
