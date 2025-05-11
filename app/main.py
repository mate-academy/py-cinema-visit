from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    for customer in range(len(customers)):
        client = Customer(
            name=customers[customer]["name"],
            food=customers[customer]["food"]
        )
        CinemaBar.sell_product(
            product=customers[customer]["food"],
            customer=client
        )

    hall = CinemaHall(number=hall_number)
    instance_customer = [
        Customer(
            name=customers[pos]["name"],
            food=customers[pos]["food"]
        )
        for pos in range(len(customers))
    ]

    hall.movie_session(
        movie,
        instance_customer,
        cleaning_staff=Cleaner(cleaner)
    )
