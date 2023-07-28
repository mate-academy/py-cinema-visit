from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner_name: str, movie: str
) -> None:
    cinema_bar = CinemaBar()

    customer_instances = [
        Customer(customer_data["name"],
                 customer_data["food"]) for customer_data in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_instances, cleaner)
