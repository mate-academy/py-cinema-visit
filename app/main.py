from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) \
        -> callable:
    customers_lst = []
    for customer in customers:
        customers_lst.append(Customer(name=customer["name"],
                                      food=customer["food"]))
    for customer_info in customers_lst:
        CinemaBar.sell_product(customer_info, customer_info.food)

    number_info = CinemaHall(hall_number)
    cleaner_info = Cleaner(cleaner)
    number_info.movie_session(movie, customers_lst, cleaner_info)
