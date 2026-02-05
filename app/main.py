from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(person)
        CinemaBar.sell_product(product=person.food, customer=person)
    hall.movie_session(movie, customers_list, cleaner_obj)
