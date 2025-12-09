from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customer_list = [
        Customer(name=customer_info["name"], food=customer_info["food"])
        for customer_info in customers
    ]

    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_list, cleaner)
