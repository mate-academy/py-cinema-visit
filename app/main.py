from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
                 customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    customer_list = []
    for customer in customers:
        customer_ins = Customer(customer["name"], customer["food"])
        customer_list.append(customer_ins)
        CinemaBar.sell_product(product=customer_ins.food, customer=customer_ins)
    hall.movie_session(movie, customer_list, cleaner_staff)
