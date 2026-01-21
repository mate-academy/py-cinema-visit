from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner_name: str,
    movie_name: str
) -> None:
    customer_instances = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers]

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)
    cinema_bar = CinemaBar()

    for customer_instance in customer_instances:
        cinema_bar.sell_product(customer_instance, customer_instance.food)

    cinema_hall.movie_session(movie_name, customer_instances, cleaner)
