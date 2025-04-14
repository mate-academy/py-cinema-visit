from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    curr_cleaner = Cleaner(cleaner)

    customers_obj_list = []
    for customer_data in customers:
        curr_customer = Customer(customer_data.get("name"),
                                 customer_data.get("food"))
        customers_obj_list.append(curr_customer)
        if curr_customer.food:
            cb.sell_product(curr_customer.food, curr_customer)

    ch.movie_session(movie, customers_obj_list, curr_cleaner)
