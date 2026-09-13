from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )

        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )

        customers_list.append(customer)

    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner,
    )
