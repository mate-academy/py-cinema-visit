from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cleaning_staff_instance = Cleaner(name=cleaner)

    costumer_instance = []
    for data in customers:
        costumer = Customer(name=data.name["name"], food=data["food"])
        costumer_instance.append(costumer)

    for costumer in costumer_instance:
        CinemaBar.sell_product(product=costumer.food, customer=costumer)

    hall_instance = CinemaHall(hall_number=hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=costumer_instance,
        cleaning_staff=cleaning_staff_instance,
    )
