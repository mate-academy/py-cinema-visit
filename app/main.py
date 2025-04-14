from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int, cleaner: str, movie: str) -> None:
    customers_inst_list = [Customer]

    cinema_bar = CinemaBar()
    for customer_dict in customers:
        if customer_dict.get("name"):
            customer_create = Customer(name=customer_dict.get("name"),
                                       food=customer_dict.get("food"))
            customers_inst_list.append(customer_create)
            cinema_bar.sell_product(customer=customer_create,
                                    product=customer_create.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_inst_list,
                              cleaning_staff=Cleaner(cleaner))
