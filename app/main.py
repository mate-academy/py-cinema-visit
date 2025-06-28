from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int, cleaner: str, movie: str) -> None:
    cinema = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)
    customer_list = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customer_list.append(new_customer)

    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)
    cinema.movie_session(movie, customer_list, cleaner_person)
