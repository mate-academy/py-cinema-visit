from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []
    for customer in customers:
        customer_person = Customer(customer["name"], customer["food"])
        list_of_customers.append(customer_person)

    cleaner_person = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in list_of_customers:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, list_of_customers, cleaner_person)
