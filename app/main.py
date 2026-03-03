from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_instances = [Customer(name=c["name"],
                                    food=c["food"]) for c in customers]
    cleaner_instance = Cleaner(name=cleaner)
    for customer in customers_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cinema_hall_instance = CinemaHall(hall_number)
    cinema_hall_instance.movie_session(movie,
                                       customers_instances,
                                       cleaner_instance)
