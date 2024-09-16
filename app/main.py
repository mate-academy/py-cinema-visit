from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for customer in customers:
        curr_customer = Customer(customer.get("name"), customer.get("food"))
        CinemaBar.sell_product(curr_customer.food, curr_customer)
        customers_list.append(curr_customer)

    hall_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, hall_cleaner)
