from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list, number: int, cleaner: str, movie: str
) -> None:
    customer_instances = [
        Customer(name=cust["name"], food=cust["food"]) for cust in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(number=number)

    cleaning_staff = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie, customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
