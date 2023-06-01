from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    cb = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))

    for customer in customers_list:
        cb.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_list, cleaner_instance)
