from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(number=hall_number)

    customer_instances = []
    for cust_dict in customers:
        new_customer = Customer(cust_dict["name"], cust_dict["food"])
        customer_instances.append(new_customer)
        # Wywołujemy metodę bezpośrednio na klasie, nie na instancji
        CinemaBar.sell_product(new_customer.food, new_customer)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
