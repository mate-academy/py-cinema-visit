from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: Cleaner,
                 movie: str) -> set:
    cleaner_instance = Cleaner(name=cleaner)

    customers_instances = [
        Customer(name=customer_info["name"], food=customer_info["food"])
        for customer_info in customers
    ]

    for customer in customers_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(hall_number=hall_number)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_instances,
                              cleaning_staff=cleaner_instance)
