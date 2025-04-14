from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:

    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    print(f'"{movie}" started in hall number {hall_number}.')

    for customer in customer_instances:
        customer.watch_movie(movie)

    print(f'"{movie}" ended.')

    cleaner = Cleaner(cleaner)
    cleaner.clean_hall(hall_number)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall
