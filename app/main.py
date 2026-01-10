from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.cinema.people.customer import Customer
from app.cinema.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int
                 , cleaner: str, movie: str) -> None:
    today_cleaner = Cleaner(cleaner)
    today_hall = CinemaHall(hall_number)
    customer_list = [Customer(today_customer["name"], today_customer["food"])
                     for today_customer in customers]
    for customer in customer_list:
        CinemaBar.sell_product(customer.name, customer.food)
    print(f'\"{movie}\" started in hall number {today_hall.hall_number}.')
    today_hall.movie_session(movie, customer_list, today_cleaner)
