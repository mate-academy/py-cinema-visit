from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str, movie: str):
    # criar objetos Customer
    customer_objects = [Customer(c['name'], c['food']) for c in customers]

    # vender produtos pelo CinemaBar (usar método estático sem instanciar)
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # criar CinemaHall e Cleaner
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    # iniciar sessão de filme
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_obj)


