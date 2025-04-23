from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers_data: list, hall_number: int, cleaner_name: str, movie: str) -> None:
    customers = [Customer(name=data["name"], food=data["food"]) for data in customers_data]
    for customer in customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cleaner = Cleaner(name=cleaner_name)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie, customers=customers, cleaning_staff=cleaner)
