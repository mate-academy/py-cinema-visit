from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    customer_list = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data.get("name", ""),
            food=customer_data.get("food", "")
        )
        cinema_bar.sell_product(customer.food, customer)
        customer_list.append(customer)

    cinema_hall.movie_session(movie, customer_list, cinema_cleaner)
