from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str, customers: list, hall_number: int,
                 cleaner: str) -> None:
    customer_class_list = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customer_class_list.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)
    schedule_movie = CinemaHall(hall_number)
    schedule_cleaning = Cleaner(cleaner)
    schedule_movie.movie_session(movie, customer_class_list, schedule_cleaning)
