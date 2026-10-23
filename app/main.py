from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for customer_dict in customers:
        customer = Customer(
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        customers_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner
    )
