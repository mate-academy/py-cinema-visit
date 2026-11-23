from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers_list = []
    for customer_loop in customers:
        customer = Customer(customer_loop["name"], customer_loop["food"])
        CinemaBar.sell_product(customer.food, customer)
        customers_list.append(customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cleaner)
