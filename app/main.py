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

    customers_list = [
        Customer(name=client["name"], food=client["food"])
        for client in customers
    ]

    purchase = CinemaBar()
    cleaner_person = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for client in customers_list:
        purchase.sell_product(product=client.food, customer=client)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_person
    )
