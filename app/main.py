from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instances = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]

        customer_instance = Customer(
            name=name,
            food=food
        )
        CinemaBar.sell_product(product=food, customer=customer_instance)
        customer_instances.append(customer_instance)

    the_cleaner = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=the_cleaner)
