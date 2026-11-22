# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str) -> None:
    customers_obj = []
    for item in customers:
        customers_obj.append(Customer(item["name"], item["food"]))
    cleaner_obj = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for customer in customers_obj:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customers_obj, cleaner_obj)
