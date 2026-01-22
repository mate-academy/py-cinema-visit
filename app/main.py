from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers_of_class_customer = []

    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        customers_of_class_customer.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)
    current_hall = CinemaHall(hall_number)
    cleaning_person = Cleaner(cleaner)
    current_hall.movie_session(movie,
                               customers_of_class_customer,
                               cleaning_person)
