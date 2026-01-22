from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances_list = []
    for customer in customers:
        customers_instances_list.append(Customer(customer.get("name"),
                                                 customer.get("food")))

    ci_hall = CinemaHall(hall_number)
    ci_bar = CinemaBar()
    ci_cleaner = Cleaner(cleaner)

    for customer in customers_instances_list:
        ci_bar.sell_product(customer.food, customer)

    ci_hall.movie_session(movie, customers_instances_list, ci_cleaner)
