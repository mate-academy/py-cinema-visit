from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    customers_list = []
    for person in customers:
        current_customer = Customer(name=person["name"], food=person["food"])
        customers_list.append(current_customer)
        cb = CinemaBar()
        cb.sell_product(current_customer, current_customer.food)

    cl = Cleaner(cleaner)
    ch = CinemaHall(hall_number)
    ch.movie_session(movie_name=movie, customers=customers_list,
                     cleaning_staff=cl)
