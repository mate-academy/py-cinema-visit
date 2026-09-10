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
    customers_instances_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    for i in range(len(customers_instances_list)):
        CinemaBar.sell_product(
            product=customers_instances_list[i].food,
            customer=customers_instances_list[i]
        )
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instances_list,
        cleaning_staff=current_cleaner
    )
