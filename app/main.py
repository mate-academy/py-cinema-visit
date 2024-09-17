from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances_list = [
        Customer(cust.get("name"),
                 cust.get("food")) for cust in customers]
    hall_is = CinemaHall(hall_number)
    bar_is = CinemaBar()
    clean = Cleaner(cleaner)
    for cust in customers_instances_list:
        bar_is.sell_product(cust.food, cust)
    hall_is.movie_session(movie,
                          customers_instances_list,
                          clean)
