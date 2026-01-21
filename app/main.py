from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    list_of_customers = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(new_customer)
    hall_num = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    for customer_of_bar in list_of_customers:
        CinemaBar.sell_product(customer_of_bar.food, customer_of_bar)
    hall_num.movie_session(movie, list_of_customers, clean)
