from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    customers_list = []

    for customer in customers:
        name = customer["name"]
        food = customer["food"]

        customer_instance = Customer(name, food)
        cinema_bar.sell_product(customer_instance, food)
        customers_list.append(customer_instance)

    cinema_hall.movie_session(
        movie_name=movie, customers=customers_list, cleaning_staff=cleaner
    )
