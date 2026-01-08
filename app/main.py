from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = []
    for objects in customers:
        customers_list.append(
            Customer(name=objects["name"],
                     food=objects["food"]
                     )
        )

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    cleaner_obj = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_obj
    )
