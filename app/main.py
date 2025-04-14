from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaning_person = Cleaner(
        name=cleaner
    )
    cinema_hall = CinemaHall(
        number=hall_number
    )

    customer_list = []
    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        customer_list.append(customer_instance)
        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaning_person
    )
