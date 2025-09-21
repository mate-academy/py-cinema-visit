from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []
    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        list_of_customers.append(person)
        CinemaBar.sell_product(product=person.food, customer=person)
    cinema_hall_number = CinemaHall(number=hall_number)
    cinema_hall_number.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=Cleaner(name=cleaner))
