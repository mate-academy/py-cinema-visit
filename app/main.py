# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    # customer es una lista de clases Customer()
    # hall_number es un entero
    # cleaner es una clase Cleaner()
    # movie es un string con el nombre de la película

    customer_list = []
    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for cust in customers:
        CinemaBar.sell_product(cust["food"], cust["name"])
        customer_instance = Customer(cust["name"], cust["food"])
        customer_list.append(customer_instance)
    hall_instance.movie_session(movie, customer_list, cleaner_instance)
