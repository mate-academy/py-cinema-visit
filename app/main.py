from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)

    customer_instances = []
    for client_data in customers:
        customer = Customer(
            name=client_data["name"],
            food=client_data["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)
    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance)
