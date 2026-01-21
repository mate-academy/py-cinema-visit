from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(person, person.food)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customers, cleaning_staff)
