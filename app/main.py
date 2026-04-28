from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    customers_list = []

    for customer in customers:
        customer_item = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        CinemaBar.sell_product(
            customer=customer_item,
            product=customer["food"]
        )
        customers_list.append(customer_item)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaning_staff
    )
