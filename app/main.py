from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    customers_list = [Customer(customer["name"], customer["food"])
                      for customer in customers]

    for customer in customers_list:
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_list, cleaner_instance)
