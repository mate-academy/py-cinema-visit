from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str,
) -> None:
    customer_list = [
        Customer(
            name=customer["name"],
            food=customer["food"],
        )
        for customer in customers
    ]

    for customer in customer_list:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )

    hall = CinemaHall(hall_number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_instance,
    )