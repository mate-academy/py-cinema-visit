from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers]
    for cust in customer_objects:
        CinemaBar.sell_product(product=cust.food, customer=cust)
    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
