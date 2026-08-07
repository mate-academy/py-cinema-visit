from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    customers_list = []
    for el in customers:
        customer = Customer(el["name"], el["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(customer, customer.food)
    (CinemaHall(hall_number).movie_session(
        movie,
        customers_list,
        Cleaner(cleaner))
     )
