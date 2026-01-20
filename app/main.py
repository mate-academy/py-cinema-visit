from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    list_of_customers = []
    for customer_dict in customers:
        list_of_customers.append(Customer(customer_dict["name"],
                                          customer_dict["food"]))

    cinema_bar = CinemaBar()

    hall = CinemaHall(hall_number)

    for customer in list_of_customers:
        cinema_bar.sell_product(customer, customer.food)

    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(movie, list_of_customers, cleaning_staff)
