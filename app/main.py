from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    new_customers = []
    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        new_customers.append(new_customer)
        CinemaBar.sell_product(customer=new_customer, product=customer["food"])
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(movie_name=movie,
                              customers=new_customers,
                              cleaning_staff=Cleaner(name=cleaner))
