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
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customer_instances = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(new_customer.food, new_customer)
        customer_instances.append(new_customer)

    cinema_hall.movie_session(movie, customer_instances, cleaning_staff)
