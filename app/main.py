from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    instance_customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    instance_cleaner = Cleaner(cleaner)

    for customer in instance_customers:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, instance_customers, instance_cleaner)
