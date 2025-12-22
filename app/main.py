from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    customers_list = []
    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        customers_list.append(customer_instance)
    cinema_hall_instance = CinemaHall(number=hall_number)
    cinema_bar_instance = CinemaBar()
    cleaner_instance = Cleaner(name=cleaning_staff)

    for customer in customers_list:
        cinema_bar_instance.sell_product(customer.food, customer)

    CinemaHall.movie_session(
        cinema_hall_instance,
        movie_name,
        customers_list,
        cleaner_instance
    )
