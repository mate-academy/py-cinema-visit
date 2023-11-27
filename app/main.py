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
    customers_inst = []
    for cust in customers:
        customers_inst.append(Customer(cust["name"], cust["food"]))
        CinemaBar.sell_product(customers_inst[-1].food, customers_inst[-1])

    cinema_hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_hall_instance.movie_session(movie, customers_inst, cleaner_instance)
