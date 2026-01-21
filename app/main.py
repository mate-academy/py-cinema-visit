from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str, customers: list, hall_number: int,
                 cleaner: str) -> None:
    new_customers = []
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        new_customers.append(customer)
    for customer in new_customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(movie_name=movie, customers=new_customers,
                       cleaning_staff=cleaner)
