from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaninig_staff: str, movie_name: str) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))

    new_bar = CinemaBar()
    for person in customer_list:
        new_bar.sell_product(person.food, person)

    new_hall_number = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaninig_staff)
    new_hall_number.movie_session(movie_name, customer_list, new_cleaner)
