from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner



def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_obj = [Customer(c["name"], c["food"]) for c in customers]
    for customer in customer_obj:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customer_obj, cleaner_obj)




