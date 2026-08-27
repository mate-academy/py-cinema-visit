from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str | None:
    customer_list = []
    for custom in customers:
        cust = Customer(custom.get("name"), custom.get("food"))
        customer_list.append(cust)
    for cust in customer_list:
        CinemaBar.sell_product(cust.food, cust)

    hall_n = CinemaHall(hall_number)
    cleaning = Cleaner(cleaner)

    hall_n.movie_session(movie, customer_list, cleaning)
