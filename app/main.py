from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for customer in customers:
        name = customer.get("name")
        food = customer.get("food")
        customer_instance = Customer(name, food)
        CinemaBar.sell_product(food, customer_instance)
        customers_list.append(customer_instance)
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cinema_cleaner)
