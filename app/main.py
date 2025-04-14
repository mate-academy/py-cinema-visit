from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(hall_number)
    customers_instances = []
    for customer in customers:
        customers_instances.append(Customer(customer["name"],
                                            customer["food"]))
    for customer_inst in customers_instances:
        CinemaBar.sell_product(customer_inst.food, customer_inst)
    hall.movie_session(movie_name=movie,
                       customers=customers_instances,
                       cleaning_staff=Cleaner(cleaner))
