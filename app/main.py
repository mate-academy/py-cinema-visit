from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(product=person.food, customer=person)
        customers_list.append(person)

    cinema_hall = CinemaHall(number=hall_number)
    current_cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_list,
                              cleaning_staff=current_cleaner)
