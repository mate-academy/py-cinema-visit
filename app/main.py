from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int, cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customers_class_instances_list = []
    for customer in customers:
        customers_class_instances_list.append(
            Customer(customer.get("name"),
                     customer.get("food")))

    for customer in customers_class_instances_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(
        movie,
        customers_class_instances_list,
        cleaning_staff
    )
