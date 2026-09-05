from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers_list = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]

        )

        customers_list.append(customer_instance)

        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance

        )

    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaning_staff
    )
