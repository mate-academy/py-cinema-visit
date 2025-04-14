from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    cinema_bar = CinemaBar()
    hall_cleaner = Cleaner(name=cleaner)

    customer_instances = []

    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        cinema_bar.sell_product(product=customer.food, customer=customer)
        customer_instances.append(customer)

    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_instances,
                              cleaning_staff=hall_cleaner)
