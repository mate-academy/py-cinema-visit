from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_of_customers = []
    cinema_bar = CinemaBar()
    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        list_of_customers.append(person)
        cinema_bar.sell_product(customer=person, product=person.food)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_cleaner = Cleaner(name=cleaner)
    cinema_hall.movie_session(movie_name=movie,
                              customers=list_of_customers,
                              cleaning_staff=cinema_cleaner)
