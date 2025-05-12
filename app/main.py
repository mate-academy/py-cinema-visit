from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    instance_customer_ = list()
    for customer in range(len(customers)):
        instance_customer_.append(
            Customer(
                name=customers[customer]["name"],
                food=customers[customer]["food"]))
        CinemaBar.sell_product(
            product=customers[customer]["food"],
            customer=instance_customer_[customer]
        )

    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie,
        instance_customer_,
        cleaning_staff=Cleaner(cleaner)
    )
