from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    cinema_bar = CinemaBar()

    for customer in customers:
        customer = Customer(
            name=customer["name"],
            food=customer["food"],
        )
        customers_list.append(customer)

        cinema_bar.sell_product(
            product=customer.food,
            customer=customer,
        )

    cleaner = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie, customers=customers_list, cleaning_staff=cleaner
    )
