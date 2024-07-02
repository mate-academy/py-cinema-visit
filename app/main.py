from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = [
        Customer(name=cust["name"], food=cust["food"])
        for cust in customers
    ]
    cinema_bar = CinemaBar()

    for customer in customer_objects:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
