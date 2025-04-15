from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_all_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    movie_hall = CinemaHall(hall_number)
    clean_master = Cleaner(cleaner)
    for cust in list_all_customers:
        CinemaBar.sell_product(cust, cust.food)
    movie_hall.movie_session(movie, list_all_customers, clean_master)
