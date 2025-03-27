from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_of_customers = []

    cinema_bar = CinemaBar()
    for person in customers:
        customer = Customer(person["name"], person["food"])
        list_of_customers.append(customer)
        cinema_bar.sell_product(customer, customer.food)

    cinema_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, list_of_customers, cinema_staff)
