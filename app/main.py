from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_list = []
    bar_sell = CinemaBar()
    for customer in customers:
        new_customer = (Customer(customer["name"], customer["food"]))
        customer_list.append(new_customer)
        bar_sell.sell_product(new_customer.food, new_customer)
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, clean)
