from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    for customer in customers:
        customer_object = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_object, customer_object.food)
        customers_list.append(customer_object)

    cinema_hall = CinemaHall(hall_number)
    cleaner_for_this_movie = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cleaner_for_this_movie)
