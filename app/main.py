from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number:
        int, cleaner: str,
        movie: str
) -> None:
    cinema_hall_obj = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    customer_obj_list = []

    for customer in customers:
        customer_obj_list.append(Customer(customer["name"], customer["food"]))

    for customer in customer_obj_list:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall_obj.movie_session(movie, customer_obj_list, cleaner_obj)
