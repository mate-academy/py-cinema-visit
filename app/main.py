from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_instance_list = []

    for customer in customers:
        customer_instance_list.append(Customer(
            customer["name"], customer["food"]))

    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer in customer_instance_list:
        CinemaBar.sell_product(customer.food, customer)

    hall_instance.movie_session(
        movie,
        customer_instance_list,
        cleaner_instance)
