from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = []
    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_stuff = Cleaner(cleaner)

    for visitor in visitors:
        cinema_bar.sell_product(visitor.food, visitor)

    cinema_hall.movie_session(movie, visitors, cleaner_stuff)
