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
    list_of_customers = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(new_customer, new_customer.food)
        list_of_customers.append(new_customer)
    cinema_hall = CinemaHall(hall_number)
    maid = Cleaner(cleaner)
    cinema_hall.movie_session(movie, list_of_customers, maid)
