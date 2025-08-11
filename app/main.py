from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objects = []
    for customer in customers:
        customer = Customer(customer.get("name"), customer.get("food"))
        CinemaBar.sell_product(product = customer.food, customer = customer)
        customer_objects.append(customer)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_objects, cleaning_staff)

    return customer_objects