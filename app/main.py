from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_stuff = Cleaner(cleaner)
    customers_inst_list = []
    for customer in customers:
        customers_inst_list.append(Customer(customer["name"],
                                            customer["food"]))

    for customer in customers_inst_list:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customers_inst_list, cleaning_stuff)
