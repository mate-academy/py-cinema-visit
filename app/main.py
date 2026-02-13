from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(
            Customer(
                name=customer["name"],
                food=customer["food"],
            )
        )

    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_instance,
    )
