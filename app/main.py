from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> None:
    customer_instances = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        customer_instances.append(customer)

    cleaner = Cleaner(name=cleaner_name)
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)  # noqa: F841

    for customer in customer_instances:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    print(f'"{movie}" started in hall number {hall_number}.')
    for customer in customer_instances:
        customer.watch_movie(movie=movie)

    print(f'"{movie}" ended.')

    cleaner.clean_hall(hall_number=hall_number)
