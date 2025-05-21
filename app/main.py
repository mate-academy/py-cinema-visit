from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(number=hall_number)
    clean_staff = Cleaner(name=cleaner)

    for customer in list_of_customers:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=clean_staff
    )
