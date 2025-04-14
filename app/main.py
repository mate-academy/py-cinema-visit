from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    for customer_dict in customers:
        customers_list.append(
            Customer(customer_dict["name"],
                     customer_dict["food"])
        )

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
