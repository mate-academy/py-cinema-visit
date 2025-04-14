from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaning_staff: str,
    movie_name: str
) -> None:
    instances = [Customer(dict["name"], dict["food"]) for dict in customers]
    cinema_hall = CinemaHall(hall_number)
    bar_info = CinemaBar()
    cleaner_person = Cleaner(cleaning_staff)
    for customer in instances:
        bar_info.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie_name, instances, cleaner_person)
