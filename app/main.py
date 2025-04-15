from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_man = Cleaner(cleaner)

    list_of_customers = []
    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        cinema_bar.sell_product(customer, customer.food)
        list_of_customers.append(customer)

    cinema_hall.movie_session(movie, list_of_customers, cleaner_man)
