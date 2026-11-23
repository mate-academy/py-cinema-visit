from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    # Create instances
    result_customers = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        ) for customer in customers
    ]
    result_cleaner = Cleaner(cleaner)
    result_cinema_hall = CinemaHall(hall_number)

    # Execution
    # Sell product
    for customer in result_customers:
        CinemaBar.sell_product(customer.food, customer)

    # Schedule a movie session
    result_cinema_hall.movie_session(
        movie_name=movie,
        customers=result_customers,
        cleaner=result_cleaner
    )
