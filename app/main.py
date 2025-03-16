from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_class_obj_list = []
    for customer in customers:
        customer_class_obj_list.append(Customer(name=customer["name"],
                                                food=customer["food"]))
    for customer in customer_class_obj_list:
        CinemaBar.sell_product(customer, customer.food)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_class_obj_list, Cleaner(cleaner))
