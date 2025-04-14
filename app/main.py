from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cinema_cleaner = Cleaner(name=cleaner)

    customers_list = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customers_list:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cinema_cleaner
    )
