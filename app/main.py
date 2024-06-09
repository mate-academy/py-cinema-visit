from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(hall_number)
    bar_ = CinemaBar()
    cleaner = Cleaner(cleaner)
    customers_list = []

    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        bar_.sell_product(customer=customer, product=customer.food)
        customers_list.append(customer)

    hall.movie_session(movie_name=movie, customers=customers_list,
                       cleaning_staff=cleaner)
