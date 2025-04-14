from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    list_of_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for client in list_of_customers:
        bar_sales = CinemaBar()
        bar_sales.sell_product(client.food, client)

    hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=cleaner
    )
