from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    client_list = [Customer(customer_new["name"],
                   customer_new["food"])
                   for customer_new in customers]
    for client in client_list:
        CinemaBar.sell_product(customer=client, product=client.food)
    CinemaHall(hall_number).movie_session(movie_name=movie,
                                          customers=client_list,
                                          cleaning_staff=Cleaner(cleaner))
