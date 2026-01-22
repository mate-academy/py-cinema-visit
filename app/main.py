from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []

    for customer in customers:
        name = customer.get("name")
        food = customer.get("food")
        customer = Customer(name, food)
        customer_instances.append(customer)
        CinemaBar.sell_product(food, customer)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customer_instances, cleaning_staff)
