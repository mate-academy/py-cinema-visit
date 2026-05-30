from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers_list = []

    for customer in customers:
        customer_item = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_item.food, customer_item)
        customers_list.append(customer_item)

    init_hall = CinemaHall(hall_number)
    init_hall.movie_session(movie, customers_list, Cleaner(cleaner))
