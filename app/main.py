from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    hall = CinemaHall(hall_number)
    bar_cinema = CinemaBar()
    cleaner_name = Cleaner(cleaner)

    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))

    for customer in customer_list:
        bar_cinema.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_list, cleaner_name)
