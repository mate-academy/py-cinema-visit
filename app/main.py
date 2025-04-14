from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    new_customer = [Customer(
        name=customer["name"],
        food=customer["food"]
    )
        for customer in customers
    ]
    hall_number = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for customer in new_customer:
        cinema_bar.sell_product(customer.food, customer)
    hall_number.movie_session(
        movie_name=movie,
        customers=new_customer,
        cleaning_staff=cleaner
    )
