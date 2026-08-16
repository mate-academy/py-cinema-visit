from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: tuple, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = [Customer(customer["name"],
                                   customer["food"]) for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for client in customer_instances:
        CinemaBar.sell_product(client.food, client)

    cinema_hall.movie_session(movie, customer_instances, cleaning_staff)
