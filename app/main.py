from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = [Customer(data["name"],
                                   data["food"]) for data in customers]
    cleaner_person = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, customer_instances, cleaner_person)
