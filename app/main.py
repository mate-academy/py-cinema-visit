from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    new_customers = []
    for human in customers:
        customer = Customer(human["name"], human["food"])
        CinemaBar.sell_product(customer, customer.food)

        new_customers.append(customer)

    this_hall = CinemaHall(hall_number)

    this_hall.movie_session(movie, new_customers, Cleaner(cleaner))
