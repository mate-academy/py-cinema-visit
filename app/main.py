from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:

    custom_inst = []
    for customer in customers:
        custom_inst.append(Customer(customer["name"], customer["food"]))

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in custom_inst:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, custom_inst, cleaner)
