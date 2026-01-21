from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str
                 ) -> None:
    list_customers = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        each_customer = Customer(name, food)
        list_customers.append(each_customer)
        CinemaBar.sell_product(food, each_customer)
    hall = CinemaHall(hall_number)
    cleaner_working = Cleaner(cleaner)
    hall.movie_session(movie, list_customers, cleaner_working)
