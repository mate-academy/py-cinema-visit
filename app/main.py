from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict], hall_number: int,
        cleaning_staff: str, movie_name: str
) -> None:
    cinema_bar: CinemaBar = CinemaBar()
    cinema_hall: CinemaHall = CinemaHall(hall_number)
    cleaner: Cleaner = Cleaner(cleaning_staff)
    customers_list = []
    for customer_info in customers:
        customer: Customer = Customer(
            customer_info["name"], customer_info["food"]
        )
        cinema_bar.sell_product(customer, customer.food)
        customers_list.append(customer)

    cinema_hall.movie_session(
        movie_name, customers_list,
        cleaner
    )
