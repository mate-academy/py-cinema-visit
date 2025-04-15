from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    list_of_customers = []
    for i in customers:
        customer = Customer(i["name"], i["food"])
        cinema_bar.sell_product(customer, customer.food)
        list_of_customers.append(customer)
    cinema_hall.movie_session(movie_name, list_of_customers, cleaner)
