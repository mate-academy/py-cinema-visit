from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar_obj = CinemaBar()
    cleaner_obj = Cleaner(cleaner)
    list_of_customers = []

    for customer_not_obj in customers:
        cs = Customer(customer_not_obj["name"], customer_not_obj["food"])
        list_of_customers.append(cs)

    for cs in list_of_customers:
        cinema_bar_obj.sell_product(cs, cs.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, list_of_customers, cleaner_obj)
