from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = [Customer(item["name"], item["food"])
                      for item in customers]
    for customer in customers_list:
        CinemaBar().sell_product(customer, customer.food)
    cleaner_ = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, customers_list, cleaner_)
