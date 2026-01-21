from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    # Create instances of Customer
    customer_objects = [Customer(name=customer["name"],
                                 food=customer["food"])
                        for customer in customers]

    # Create instance of Cleaner
    cleaner_instance = Cleaner(name=cleaner)

    # Sell food to customers
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Create instance of CinemaHall
    hall = CinemaHall(number=hall_number)

    # Start movie session
    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_instance)
    pass
