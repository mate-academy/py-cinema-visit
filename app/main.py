from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list
                 , hall_number: int
                 , cleaner: str
                 , movie: str
                 ) -> None:
    today_cleaner = Cleaner(cleaner)
    today_hall = CinemaHall(hall_number)
    cb = CinemaBar()
    customer_list = [Customer(today_customer["name"], today_customer["food"])
                     for today_customer in customers]
    for customer in customer_list:
        cb.sell_product(customer.name, customer.food)
    today_hall.movie_session(movie, customer_list, today_cleaner)
