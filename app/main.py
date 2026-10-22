from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_instances = [
        Customer(
            name=customer_data["name"],
            food=customer_data["food"],
        )
        for customer_data in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food,
        )

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff,
    )
