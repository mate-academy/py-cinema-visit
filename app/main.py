# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
