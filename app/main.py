from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_of_customers = []
    bar = CinemaBar()
    for item in customers:
        customer = Customer(item["name"], item["food"])
        list_of_customers.append(customer)
        bar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, list_of_customers, cleaning_staff)
