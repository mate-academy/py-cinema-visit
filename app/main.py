from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    new_customer = []
    for client in customers:
        customer_info = Customer(client["name"], client["food"])
        new_customer.append(customer_info)
        CinemaBar.sell_product(customer_info, client["food"])
    cleaning = Cleaner(cleaner)
    class_hall = CinemaHall(hall_number)
    class_hall.movie_session(movie, new_customer, cleaning)
