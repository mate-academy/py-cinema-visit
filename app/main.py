from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str
) -> None:
    customers_inst = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in customers_inst:
        CinemaBar.sell_product(customer, customer.food)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customers_inst, cleaner)
