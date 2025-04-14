from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[Customer],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_bar = CinemaBar()
    customers_list = []
    cleaner = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    for customers_info in customers:
        customer = Customer(name=customers_info["name"],
                            food=customers_info["food"])
        cinema_bar.sell_product(customer=customer,
                                product=customer.food)
        customers_list.append(customers_info)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner
    )
