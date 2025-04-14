from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    customers_insts = []
    for customer in customers:
        customer_inst = Customer(name=customer["name"], food=customer["food"])
        customers_insts.append(customer_inst)
        cinema_bar.sell_product(customer_inst.food, customer_inst)
    cinema_hall.movie_session(movie, customers_insts, cleaner)
