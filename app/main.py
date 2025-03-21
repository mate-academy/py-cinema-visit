from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        cinembar = CinemaBar(product=customer.food, customer=customer.name)
        print(cinembar.sell_product())

    hall = CinemaHall(hall_number=hall_number)

    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customers=customers, cleaning_staff=cleaning_staff)


customers = [
    Customer(name="Bob", food="Coca-cola"),
    Customer(name="Alex", food="popcorn")
]

cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
