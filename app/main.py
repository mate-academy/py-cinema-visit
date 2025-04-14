from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_list = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        customer_in_list = Customer(name, food)
        customer_list.append(customer_in_list)
        CinemaBar.sell_product(food, customer_in_list)
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_list, cleaning_staff)
