from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict[str, str]], hall_number: int, cleaner: str, movie: str
) -> None:

    customers_list = [
        Customer(name=customer.get("name", ""), food=customer.get("food", ""))
        for customer in customers
    ]

    for customer in customers_list:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )

    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=Cleaner(name=cleaner),
    )
