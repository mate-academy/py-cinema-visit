from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str) -> None:
    # Step 1: Create Customer instances
    customer_objects = [Customer(name=c["name"],
                                 food=c["food"]) for c in customers]

    # Step 2: Sell food immediately after creating customers
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Step 3: Create CinemaHall and Cleaner instances
    hall = CinemaHall(hall_number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    # Step 4: Schedule movie session
    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_obj)
