from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitor = []
    for customer in customers:
        visitors = Customer(name=customer["name"], food=customer["food"])
        visitor.append(visitors)
        CinemaBar.sell_product(visitors, visitors.food)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, visitor, Cleaner(cleaner))
