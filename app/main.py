from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    """
        making from dict Object of class customer.
        loop in list of objects . Gives to module bar instance of Customer,
        and instance.food : name of food
        to module hall to Class CinemaHall gives number of table.
        to module cinema_staff gives name of Cleaner
        Starting movie session in module Hall. -> gives parameters:
        movie, list of class object, instance of class CLeaner

    :param customers:  dict {"name" : "name" , "food" : "food"}
    :param hall_number: int number of hall
    :param cleaner: str name of Cleaner
    :param movie: str name of movie
    :return: None
    """
    customer_objects = [Customer(person["name"], person["food"])
                        for person in customers]
    for customer in customer_objects:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customer_objects, cleaner)
