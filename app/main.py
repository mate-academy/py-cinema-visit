from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = [
        Customer(name=cust["name"], food=cust["food"])
        for cust in customers
    ]

    cleaning_staff = Cleaner(name=cleaner)

    cinema_hall = CinemaHall(number=number)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_objects,
                              cleaning_staff=cleaning_staff)
