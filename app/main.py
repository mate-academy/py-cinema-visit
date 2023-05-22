from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    people = [Customer(customer["name"], customer["food"])
              for customer in customers]
    bar_visit = CinemaBar()
    [bar_visit.sell_product(customer, customer.food) for customer in people]
    cinema = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    cinema.movie_session(movie, people, clean)
