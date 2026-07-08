from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    cleaner_instance = Cleaner(name=cleaner)

    hall_instance = CinemaHall(number=hall_number)

    customer_instances = []
    for cust_dict in customers:
        customer_obj = Customer(name=cust_dict["name"], food=cust_dict["food"])
        customer_instances.append(customer_obj)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
