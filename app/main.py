from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers_list = [Customer(customer_dict["name"],
                               customer_dict["food"]
                               ) for customer_dict in customers]
    hall = CinemaHall(hall_number)
    cleaner_cls = Cleaner(cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customers_list, cleaner_cls)
