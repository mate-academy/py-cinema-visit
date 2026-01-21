from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = [Customer(customer["name"], customer["food"]) for customer
                      in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customers_list:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, customers_list, cleaner_staff)
