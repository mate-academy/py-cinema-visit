from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer_list = []
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for person in customers:
        customer_p = Customer(person["name"], person["food"])
        customer_list.append(customer_p)

        cinema_bar.sell_product(customer_p, customer_p.food)

    cinema_hall.movie_session(movie, customer_list, cleaner_instance)
