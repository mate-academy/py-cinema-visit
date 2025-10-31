from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str,
                ) -> None:
    customer_instances = []

    for customer_data in customers:
        customer_instance = Customer(name=customer_data["name"],
                                     food=customer_data["food"])
        customer_instances.append(customer_instance)
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        cleaning_staff=cleaning_staff,
        customers=customer_instances
    )
