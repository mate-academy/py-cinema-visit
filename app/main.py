from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_instances = [Customer(
        name=customer["name"],
        food=customer["food"])
        for customer in customers]
    cinema_hall_instances = CinemaHall(number=hall_number)
    cleaner_instances = Cleaner(cleaner)
    for customer in customers_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    CinemaHall.movie_session(
        cinema_hall_instances,
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner_instances)
