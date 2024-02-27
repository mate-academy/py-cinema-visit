from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(new_customer)

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)
    for person in list_of_customers:
        cinema_bar.sell_product(person.food, person)
    cinema_hall.movie_session(movie, list_of_customers, cinema_cleaner)
