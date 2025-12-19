from app.cinema.bar import CinemaBar
from app.cinema.hell import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


customer = Customer()
hall_number = CinemaHall()
cleaner = Cleaner()



def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    CinemaBar.sell_product(customer)
    hall_number.movie_session(movie, customers, cleaner)
