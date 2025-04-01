from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str, movie: str):
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    customer_instances = []
    for customer_data in customers:
        customer = Customer(customer_data['name'], customer_data['food'])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall.movie_session(cinema_hall, movie, customer_instances, cleaner_instance)
