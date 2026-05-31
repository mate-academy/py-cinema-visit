from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(number=hall_number)
    cleaner_name = Cleaner(name=cleaner)
    visitors = []
    for customer in customers:
        visitors.append(Customer(name=customer["name"], food=customer["food"]))
    for visitor in visitors:
        CinemaBar.sell_product(visitor, visitor.food)

    hall.movie_session(movie, visitors, cleaner_name)
