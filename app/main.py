from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customer_list = []
    for customer_info in customers:
        customer = Customer(
            name=customer_info["name"],
            food=customer_info["food"],
        )
        customer_list.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner
    )
