from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:
    list_of_customers = [Customer(name_n_food["name"],
                                  name_n_food["food"])
                         for name_n_food in customers]
    for customer in list_of_customers:
        CinemaBar.sell_product(customer.food, customer)
    cinema_instance = CinemaHall(hall_number)
    staff_instance = Cleaner(cleaning_staff)
    cinema_instance.movie_session(movie_name,
                                  list_of_customers, staff_instance)
