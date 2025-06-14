from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instance = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        customer_instance.append(customer)
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)
    for customer_inst in customer_instance:
        CinemaBar.sell_product(customer_inst.food, customer_inst)
    hall_instance.movie_session(movie, customer_instance, cleaner_instance)
