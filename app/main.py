from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: [dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    customers_list = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    for customer in customers_list:
        CinemaBar().sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(
        movie_name,
        customers_list,
        Cleaner(cleaning_staff)
    )
