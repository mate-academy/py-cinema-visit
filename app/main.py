from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict[str, str]], hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cleaner_inst = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    customers_inst = []

    for customer in customers:
        customer_inst = Customer(customer["name"], customer["food"])
        customers_inst.append(customer_inst)

        cinema_bar.sell_product(customer["food"], customer_inst)

    hall.movie_session(movie, customers_inst, cleaner_inst)
