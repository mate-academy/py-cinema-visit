from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie_name: str) -> None:
    customer_instances = [
        Customer(param["name"], param["food"]) for param in customers]
    cinema_bar = CinemaBar()
    cleaning_staff = Cleaner(cleaner)

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie_name, customer_instances, cleaning_staff)
