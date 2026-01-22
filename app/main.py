from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances = []

    for instance in customers:
        customers_instances.append(Customer(name=instance["name"],
                                            food=instance["food"]))

    cinema = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar
    cleaner_name = Cleaner(name=cleaner)

    for sell in customers_instances:
        cinema_bar.sell_product(sell, sell.food)

    cinema.movie_session(movie_name=movie,
                         customers=customers_instances,
                         cleaning_staff=cleaner_name)
