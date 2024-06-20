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
    customers_instances = [
        Customer(name=person["name"], food=person["food"])
        for person in customers
    ]
    new_hall = CinemaHall(number=hall_number)
    new_bar = CinemaBar()
    new_cleaner = Cleaner(cleaner)

    for customer in customers_instances:
        new_bar.sell_product(customer, customer.food)

    CinemaHall.movie_session(
        self=new_hall,
        movie_name=movie,
        customers=customers_instances,
        cinema_staff=new_cleaner
    )
