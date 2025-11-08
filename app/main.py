from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str) -> None:
    customer_instance = []
    for customer_data in customers:
        customer_obj = Customer(name=customer_data["name"],
                                food=customer_data["food"])
        customer_instance.append(customer_obj)

    for customer_obj in customer_instance:
        CinemaBar.sell_product(customer=customer_obj,
                               product=customer_obj.food)

    hall_cinema = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall_cinema.movie_session(movie_name=movie, customers=customer_instance,
                              cleaning_staff=cleaning_staff)
