from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str, movie: str) -> None:
    list_of_customers = [Customer(i["name"], i["food"]) for i in customers]
    for i in list_of_customers:
        CinemaBar.sell_product(Customer(i.name, i.food), i.food)
    CinemaHall(hall_number).movie_session(
        movie,
        list_of_customers,
        Cleaner(cleaner))
