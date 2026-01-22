from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []
    cb = CinemaBar()
    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        list_of_customers.append(person)
        cb.sell_product(customer=person, product=person.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=cleaning_staff
    )
