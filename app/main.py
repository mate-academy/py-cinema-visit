from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    # Create Customer instances
    customer_objects = [Customer(name=c["name"],
                                 food=c["food"]) for c in customers]

    # Create Cleaner instance
    cleaner_obj = Cleaner(name=cleaner)

    # Create CinemaHall instance
    hall = CinemaHall(number=hall_number)

    # Sell food to each customer and print the result
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Start movie session
    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_obj)
