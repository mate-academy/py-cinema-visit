from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    people = [Customer(customer["name"], customer["food"])
              for customer in customers]
    cleaner_staff = Cleaner(cleaner)

    for customer in people:
        CinemaBar.sell_product(customer.name, customer.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, people, cleaner_staff)
