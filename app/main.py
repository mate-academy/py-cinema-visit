from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_staff = Cleaner(cleaner)
    customers_list = []

    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customers_list.append(customer_instance)
        cinema_bar.sell_product(customer_instance.food, customer_instance)

    cinema_hall.movie_session(movie, customers_list, cinema_staff)
