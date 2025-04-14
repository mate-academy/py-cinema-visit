from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    customer_lst = [
        Customer(
            name=customer["name"], food=customer["food"]
        ) for customer in customers
    ]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner_ = Cleaner(name=cleaner)
    for customer in customer_lst:
        cinema_bar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(
        movie_name=movie, customers=customer_lst, cleaning_staff=cleaner_
    )
