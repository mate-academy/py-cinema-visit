from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instances = [Customer(customer["name"], customer["food"])
                          for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer_instance in customer_instances:
        CinemaBar.sell_product(customer_instance.food, customer_instance)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
