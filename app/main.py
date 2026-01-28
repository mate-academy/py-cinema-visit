from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    customers_instances = [
        Customer(name=cd["name"],
                 food=cd["food"]
                 )
        for cd in customers
    ]
    for customer in customers_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner_instance
    )
