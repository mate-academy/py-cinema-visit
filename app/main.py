from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    customers_instance_list = []
    for customer in customers:
        customers_instance_list.append(
            Customer(customer["name"], customer["food"])
        )
    for customer_instance in customers_instance_list:
        cinema_bar.sell_product(customer_instance, customer_instance.food)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instance_list,
        cleaning_staff=clean,
    )
