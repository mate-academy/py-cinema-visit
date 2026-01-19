from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers_list = [Customer(name=client["name"], food=client["food"])
                      for client in customers]

    cinema_hall = CinemaHall(hall_number)
    cleaner_worker = Cleaner(cleaner)

    for client in customers_list:
        CinemaBar.sell_product(
            customer=client,
            product=client.food
        )
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_worker
    )
