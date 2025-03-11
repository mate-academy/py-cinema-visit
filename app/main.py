from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int, cleaner: str,
                 movie: str) -> None:
    lst_customers = []
    for customer in customers:
        cust_instance = Customer(customer["name"], customer["food"])
        lst_customers.append(cust_instance)

    for customer in lst_customers:
        cinema_bar_instance = CinemaBar()
        cinema_bar_instance.sell_product(customer.food, customer)

    cleaner = Cleaner(cleaner)
    cinema_customer_instance = CinemaHall(hall_number)
    cinema_customer_instance.movie_session(movie, lst_customers, cleaner)
