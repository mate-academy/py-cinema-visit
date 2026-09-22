from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    customer_instances: list[Customer] = []
    for customer in customers:
        visiter_cinema = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(visiter_cinema.food, visiter_cinema)
        customer_instances.append(visiter_cinema)

    cinema_hall = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customer_instances, cleaner_person)
