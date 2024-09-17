from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str
                 ) -> None:
    customers_instances = [Customer(customer["name"],
                           customer["food"]) for customer in customers]
    for cust in customers_instances:
        CinemaBar.sell_product(cust.food, cust)
    cleaning_staff = Cleaner(cleaner)
    hall_instances = CinemaHall(hall_number)
    hall_instances.movie_session(movie_name=movie,
                                 customers=customers_instances,
                                 cleaning_staff=cleaning_staff)
