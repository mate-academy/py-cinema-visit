from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_class = CinemaHall(number=hall_number)
    cleaner_class = Cleaner(name=cleaner)
    customers_list = []
    for customer_data in customers:
        customer_class = Customer(
            name=customer_data["name"], food=customer_data["food"]
        )
        CinemaBar.sell_product(
            product=customer_class.food,
            customer=customer_class
        )
        customers_list.append(customer_class)

    cinema_class.movie_session(
        customers=customers_list,
        cleaning_staff=cleaner_class,
        movie_name=movie
    )
