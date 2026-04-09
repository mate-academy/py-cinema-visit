from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    customers_obj_list = []
    # print(customers)

    # classes initialization
    if customers:
        for customer in customers:
            customer_obj = Customer(customer["name"], customer["food"])
            customers_obj_list.append(customer_obj)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    # calling methods
    for customer_obj in customers_obj_list:
        CinemaBar.sell_product(customer_obj, customer_obj.food)
    CinemaHall.movie_session(
        cinema_hall,
        movie=movie,
        customers=customers_obj_list,
        cleaning_staff=cleaner
    )
