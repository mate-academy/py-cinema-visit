from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customers_list = []
    for customer_dict in customers:
        obj = Customer(name=customer_dict["name"], food=customer_dict["food"])
        customers_list.append(obj)
    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_list, cleaning_staff)
