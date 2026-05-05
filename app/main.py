from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for current_customer in customers_list:
        CinemaBar.sell_product(
            customer=current_customer,
            product=current_customer.food
        )

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=Cleaner(cleaner)
    )
