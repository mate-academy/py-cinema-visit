from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    # 1. Create instances of Customer
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    # 2. Create instances of Cleaner and CinemaHall
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)

    # 3. Sell food using CinemaBar's static method
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # 4. Run the movie session
    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
