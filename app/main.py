from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []

    for customer in customers:
        customers_list.append(
            Customer(name=customer["name"],
                     food=customer["food"])
        )

    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(number=hall_number)

    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(
        movie=movie,
        customers=customers_list,
        cleaning_staff=cleaner_obj
    )
