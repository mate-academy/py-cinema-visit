from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                hall_number: int,
                cleaner: str,
                movie: str) -> None:
    customers_objs = [Customer(customer["name"], customer["food"])
                        for customer in customers]

    hall = CinemaHall(hall_number)

    cleaner_hall = Cleaner(cleaner)

    for customer in customers_objs:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall.movie_session(movie_name=movie,
                        customers=customers_objs,
                        cleaning_staff=cleaner_hall)
