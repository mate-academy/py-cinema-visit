from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    instances_customers = [
        Customer(cust["name"], cust["food"])
        for cust in customers
    ]

    instance_hall = CinemaHall(hall_number)

    instance_cleaner = Cleaner(cleaner)

    for instance_customer in instances_customers:
        CinemaBar.sell_product(instance_customer, instance_customer.food)

    instance_hall.movie_session(movie, instances_customers, instance_cleaner)
