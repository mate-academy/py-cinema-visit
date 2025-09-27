from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list["Customer"]
                 , hall_number: int, cleaner: str, movie: str) -> None:
    for customer in customers:
        cleaner = Cleaner(cleaner)
        hall = CinemaHall(hall_number)
        CinemaBar.sell_product(customer.name, customer.food)
        hall.movie_session(movie, customers, cleaner)
