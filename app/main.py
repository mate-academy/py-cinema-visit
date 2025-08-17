from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str, customers: list[dict], hall_number: int, cleaner: str
) -> None:
    # Create Customer instances
    customers_instances = [
        Customer(name=cust['name'], food=cust['food']) for cust in customers
    ]

    # Create Cleaner instance
    cleaner_instance = Cleaner(name=cleaner, hall_number=hall_number)

    # Serve food to each customer
    for customer_instance in customers_instances:
        CinemaBar.sell_product(
            product=customer_instance.food, customer=customer_instance
        )

    # Create CinemaHall instance and start movie session
    cinema_hall = CinemaHall(hall_number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner_instance
    )
