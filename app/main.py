from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str
                 ) -> None:
    customer_instances = [Customer
                          (customer["name"],
                           customer["food"])
                          for customer in customers]

    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaning_staff)

    for customer in customer_instances:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(movie_name, customer_instances, cleaner)
