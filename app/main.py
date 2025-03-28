from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[Customer],
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:

    hall = CinemaHall(number=hall_number)

    snack_bar = CinemaBar()

    cleaner = Cleaner(name=cleaning_staff)

    cinema_customers = []

    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        snack_bar.sell_product(customer=customer, product=customer.food)
        cinema_customers.append(customer)

    hall.movie_session(movie_name=movie_name,
                       customers=cinema_customers,
                       cleaning_staff=cleaner)
