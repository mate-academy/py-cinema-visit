from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str,
                 customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 ) -> None:
    customer_instances = [Customer(i["name"], i["food"]) for i in customers]
    ch = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customer_instances:
        CinemaBar.sell_product(customer, customer.food)
    ch.movie_session(movie, customer_instances, cleaner)
