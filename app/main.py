from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    cinema_bar = CinemaBar()
    for person in customers:
        customer = Customer(person.get("name"), person.get("food"))
        customers_list.append(customer)
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall = CinemaHall(hall_number)
    cleaning_person = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cleaning_person)
