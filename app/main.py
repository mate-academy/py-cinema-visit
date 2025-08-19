from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    all_customers = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        all_customers.append(new_customer)
    cleaning = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    for people in all_customers:
        CinemaBar.sell_product(people.food, people)
    cinema_hall.movie_session(movie, all_customers, cleaning)