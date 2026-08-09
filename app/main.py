from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_list = []
    for customer in customers:
        customer_object = Customer(customer["name"], customer["food"])
        customer_list.append(customer_object)
        CinemaBar.sell_product(customer_object.food, customer_object)
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cleaning_staff)
