from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall_number = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    customer_list = []
    for customer_dict in customers:
        customer = Customer(
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        customer_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    hall_number.movie_session(movie, customer_list, cleaner)
