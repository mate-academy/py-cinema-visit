from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:
    customer_list = []

    for client in customers:
        new_client = Customer(name=client["name"], food=client["food"])
        CinemaBar.sell_product(new_client, client["food"])
        customer_list.append(new_client)

    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner_name)
    cinema_hall.movie_session(movie, customer_list, cleaning_staff)
