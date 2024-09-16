from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_customer = []

    for client in customers:

        info_customer = Customer(name=client["name"],
                                 food=client["food"])

        list_customer.append(info_customer)

        CinemaBar.sell_product(client["food"], info_customer)

    cleaning = Cleaner(cleaner)

    num_hall = CinemaHall(hall_number)

    CinemaHall.movie_session(num_hall,
                             movie_name=movie,
                             customers=list_customer,
                             cleaning_staff=cleaning)
