from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_instances = [
        Customer
        (
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        for customer_dict in customers
    ]
    cleaner_instance = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in customers_instances:
        CinemaBar.sell_product(
            customer.food,
            customer
        )
    cinema_hall.movie_session(movie, customers_instances, cleaner_instance)
