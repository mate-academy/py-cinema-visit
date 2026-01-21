from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        CinemaBar.sell_product(customer=customer, product=customer.food)
        customer_list.append(customer)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_list, Cleaner(cleaner))
