from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner_name)
    customer_list = [Customer(customer["name"], customer["food"])
                     for customer in customers]
    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_list, cleaning_staff)
    pass
