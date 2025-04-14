from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instance_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    [
        CinemaBar.sell_product(customer, customer.food)
        for customer in customer_instance_list
    ]

    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    cinema_hall.movie_session(
        movie, customer_instance_list, cleaner_instance
    )
