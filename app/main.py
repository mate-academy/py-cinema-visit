from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_list:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food
        )

    cleaner_name = cleaner
    cleaner = Cleaner(cleaner_name)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, cleaner)
