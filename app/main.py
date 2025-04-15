from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:

    customers_list = []
    for person in customers:
        customer = Customer(person["name"], person["food"])
        CinemaBar.sell_product(customer.food, customer)
        customers_list.append(customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name, customers_list, Cleaner(cleaning_staff))
