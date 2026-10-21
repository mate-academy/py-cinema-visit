from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    new_list = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        new_list.append(new_customer)
    for cinema_customer in new_list:
        CinemaBar.sell_product(cinema_customer.food, cinema_customer)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, new_list, cleaning_staff)
