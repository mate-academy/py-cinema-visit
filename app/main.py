from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    # Create Customer objects from the list of dictionaries
    customer_objects = [Customer(c["name"],
                                 c["food"]) for c in customers]

    # Create CinemaHall and Cleaner objects
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # Sell food to customers at the cinema bar
    for cust in customer_objects:
        CinemaBar.sell_product(cust.food, cust)

    # Schedule the movie session and clean the hall after the movie
    hall.movie_session(movie, customer_objects, cleaning_staff)
