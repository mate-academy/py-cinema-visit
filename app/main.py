from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner_name: str,
        movie_name: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaners = Cleaner(cleaner_name)
    customer_list = [
        Customer(customer.get("name"),
                 customer.get("food"))
        for customer in customers
    ]
    for customer in customer_list:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(
        movie_name, customer_list, cleaners)
