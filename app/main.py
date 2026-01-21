from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_customers = [Customer(customer["name"], customer["food"])
                      for customer in customers]

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    for client in list_customers:
        cinema_bar.sell_product(customer=client, product=client.food)
    cinema_hall.movie_session(movie_name=movie,
                              customers=list_customers,
                              cleaning_staff=cleaner)
