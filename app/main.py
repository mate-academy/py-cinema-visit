# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    day_customers = []
    for customer in customers:
        day_customers.append(Customer(customer["name"], customer["food"]))

    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    bar_service = CinemaBar
    for customer in day_customers:
        bar_service.sell_product(customer, customer.food)

    hall.movie_session(movie, day_customers, cleaner_staff)
