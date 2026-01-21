from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    # Create CinemaBar instance
    cinema_bar = CinemaBar()

    # Sell food to customers
    for customer_info in customers:
        customer = Customer(
            name=customer_info["name"], food=customer_info["food"]
        )
        cinema_bar.sell_product(customer=customer, product=customer.food)

    # Create CinemaHall instance
    cinema_hall = CinemaHall(number=hall_number)

    # Create Cleaner instance
    cleaner_instance = Cleaner(name=cleaner)

    # Start movie session
    cinema_hall.movie_session(
        movie_name=movie,
        customers=[
            Customer(name=customer_info["name"], food=customer_info["food"])
            for customer_info in customers
        ],
        cleaning_staff=cleaner_instance
    )
