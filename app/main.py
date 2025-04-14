from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: str,
                 cleaner: str,
                 movie: str) -> None:

    customer_instances = [Customer(name=customer["name"],
                                   food=customer["food"]
                                   ) for customer in customers]

    cleaner_instance = Cleaner(name=cleaner)

    hall_instance = CinemaHall(number=hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall_instance.movie_session(movie_name=movie,
                                customers=customer_instances,
                                cleaning_staff=cleaner_instance)
