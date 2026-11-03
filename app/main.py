from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    movie: str,
    customers: list[dict],
    hall_number: int,
    cleaner: str
) -> None:
    customer_list = [
        Customer(name=person["name"], food=person["food"])
        for person in customers
    ]

    for customer in customer_list:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaning_staff
    )
