from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_inst_list = []
    for cust in customers:
        new_cust = Customer(name=cust["name"], food=cust["food"])
        CinemaBar.sell_product(new_cust.food, new_cust)
        customers_inst_list.append(new_cust)
    cleaner_inst = Cleaner(cleaner)
    hall_inst = CinemaHall(hall_number)
    hall_inst.movie_session(movie, customers_inst_list, cleaner_inst)
