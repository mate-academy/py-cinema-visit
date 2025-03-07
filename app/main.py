from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = [Customer(customer_info["name"], customer_info["food"])
                      for customer_info in customers]

    bar_sell = CinemaBar()
    [bar_sell.sell_product(customer_info, customer_info.food)
     for customer_info in customers_list]

    cinema_hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cleaner_name)
