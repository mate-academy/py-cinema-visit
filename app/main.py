from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cleaner_obj = Cleaner(cleaner)
    list_of_customer_obj = []

    for person in customers:
        list_of_customer_obj.append(Customer(person["name"], person["food"]))

    for person in customers:
        visitor = Customer(person["name"], person["food"])
        CinemaBar.sell_product(visitor, visitor.food)

    CinemaHall(hall_number).movie_session(movie,
                                          list_of_customer_obj,
                                          cleaner_obj)
