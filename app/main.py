from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    number = CinemaHall(hall_number)
    isinstance(cleaner, Cleaner)
    cl_name = Cleaner(cleaner)
    customers_res = []
    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        customers_res.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)
    (CinemaHall.movie_session(self=number
                              , movie_name=movie
                              , customers=customers_res
                              , cleaning_staff=cl_name))
