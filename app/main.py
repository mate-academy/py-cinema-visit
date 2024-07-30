from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str,
) -> None:
    customers_insts = []

    for customer in customers:
        customer_inst = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_inst, customer_inst.food)

        customers_insts.append(customer_inst)

    cinema_hall_inst = CinemaHall(hall_number)
    cleaner_inst = Cleaner(cleaning_staff)
    cinema_hall_inst.movie_session(movie_name, customers_insts, cleaner_inst)
