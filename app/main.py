from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)
    customer_instances = [Customer(name=c["name"],
                                   food=c["food"]) for c in customers]
    bar_instance = CinemaBar()

    for customer in customer_instances:
        bar_instance.sell_product(product=customer.food, customer=customer)

    hall_instance.movie_session(movie_name=movie,
                                customers=customer_instances,
                                cleaning_staff=cleaner_instance)
