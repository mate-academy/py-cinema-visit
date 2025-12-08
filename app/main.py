from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = []
    for customer_data in customers:
        cust_instance = Customer(name=customer_data["name"],
                                 food=customer_data["food"])
        customer_instances.append(cust_instance)
        CinemaBar.sell_product(product=customer_data["food"],
                               customer=cust_instance)

    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)
    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
