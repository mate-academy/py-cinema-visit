from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> None:

    hall = CinemaHall(hall_number)
    bar_func = CinemaBar()
    cleaning = Cleaner(cleaner_name)
    list_of_customer = []

    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        list_of_customer.append(customer)
        bar_func.sell_product(product=customer_info["food"], customer=customer)

    CinemaHall.movie_session(self=hall, movie_name=movie,
                             customers=list_of_customer,
                             cleaning_staff=cleaning)
