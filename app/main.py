from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_group = [Customer(name = cust["name"], food = cust["food"]) for cust in customers]
    for client in customer_group:
        CinemaBar.sell_product(product = client.food, customer = client)
    hall = CinemaHall(hall_number = hall_number)
    cleaner_staff = Cleaner(name = cleaner)
    hall.movie_session(
        movie_name=movie,
        customers = customer_group,
        cleaning_staff = cleaner_staff)
