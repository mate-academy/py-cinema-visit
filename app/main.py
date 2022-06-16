from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    list_of_customers = []
    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        list_of_customers.append(customer)
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, list_of_customers, cleaning_staff)
