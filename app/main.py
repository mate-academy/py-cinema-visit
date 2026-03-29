from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: str,
        cleaner: str,
        movie: str
) -> None:

    customer_instances = [
        Customer(data["name"], data["food"]) for data in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    hall.movie_session(movie, customer_instances, cleaner_instance)
