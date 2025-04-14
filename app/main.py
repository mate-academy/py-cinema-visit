# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list
                 , hall_number: int
                 , cleaner: str
                 , movie: str) -> None:
    customer_list = []
    for customer_data in customers:
        new_customer = Customer(customer_data["name"], customer_data["food"])
        customer_list.append(new_customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_list, cleaner)
