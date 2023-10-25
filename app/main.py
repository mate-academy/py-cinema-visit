# write your imports here
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    # write you code here
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customers_class_instances_list = [Customer(customer.get("name"),
                                      customer.get("food"))
                                      for customer in customers]

    for customer in customers_class_instances_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(
        movie,
        customers_class_instances_list,
        cleaning_staff
    )
