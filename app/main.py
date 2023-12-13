from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    list_of_customers = []

    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(new_customer)
        CinemaBar.sell_product(new_customer, new_customer.food)

    movie_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    movie_hall.movie_session(movie_name, list_of_customers, cleaner)
