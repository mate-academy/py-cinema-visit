from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_inst = [
        Customer(customer_dict["name"], customer_dict["food"])
        for customer_dict in customers
    ]
    for customer_inst in customers_inst:
        food = customer_inst.food
        CinemaBar.sell_product(customer_inst, food)
    cinema_hall_inst = CinemaHall(hall_number)
    cleaner_inst = Cleaner(cleaner)
    cinema_hall_inst.movie_session(movie, customers_inst, cleaner_inst)
    pass
