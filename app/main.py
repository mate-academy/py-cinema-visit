from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:

    cinema_hall = CinemaHall(hall_number)
    cleaner_list = Cleaner(cleaning_staff)

    customer_list = []
    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        customer_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie_name, customer_list, cleaner_list)
