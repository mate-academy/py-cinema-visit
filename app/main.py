from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cleaner_obj = Cleaner(cleaner)
    customer_list = []

    for cust in customers:

        customer_obj = Customer(cust["name"], cust["food"])
        CinemaBar().sell_product(customer_obj, customer_obj.food)
        customer_list.append(customer_obj)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_list, cleaner_obj)
