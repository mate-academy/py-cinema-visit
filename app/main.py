from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaning_stuff = Cleaner(cleaner)
    new_customers = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(new_customer, new_customer.food)
        new_customers.append(new_customer)
    cinema_hall.movie_session(movie, new_customers, cleaning_stuff)
