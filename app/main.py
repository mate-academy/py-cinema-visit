from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instance_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_instance_list:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall = CinemaHall(hall_number)
    cleaning_stuff = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customers_instance_list, cleaning_stuff)
