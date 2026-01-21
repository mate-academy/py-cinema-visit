from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = []
    for customer in customers:
        customers_list.append(Customer(customer.get("name"),
                                       customer.get("food")))
    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(movie, customers_list,
                                          Cleaner(cleaner))
