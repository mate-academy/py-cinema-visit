from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str
) -> None:
    if not isinstance(customers, list):
        (hall_number, cleaner, movie, customers) = (
            customers, hall_number, cleaner, movie
        )
    result_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    for result_customer in result_customers:
        CinemaBar.sell_product(
            product=result_customer.food,
            customer=result_customer
        )
    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=result_customers,
        cleaning_staff=cleaning_staff
    )
