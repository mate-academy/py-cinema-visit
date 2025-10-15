from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str, customers: list,
        hall_number: int, cleaner: str
) -> None:

    customer_instances = []
    for customer_data in customers:
        customer_instance = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        customer_instances.append(customer_instance)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
