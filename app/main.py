from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    list_customers = []
    cinema_bar = CinemaBar()
    for client in customers:
        human = Customer(client["name"], client["food"])
        list_customers.append(human)
        cinema_bar.sell_product(human, human.food)

    hall = CinemaHall(hall_number)
    cleaning = Cleaner(cleaner)
    hall.movie_session(movie, list_customers, cleaning)
