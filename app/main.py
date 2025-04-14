from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:

    cleaner_instance = Cleaner(name=cleaner)

    customer_instances = [Customer(name=customer["name"],
                                   food=customer["food"])
                          for customer in customers]

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
