from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:

    customer_objects = []
    for data in customers:
        cus = Customer(name=data["name"], food=data["food"])
        customer_objects.append(cus)

    for cus in customer_objects:
        CinemaBar.sell_product(product=cus.food, customer=cus)

    cleaning_staff = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
