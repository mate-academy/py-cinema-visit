from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    list_of_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers]
    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaner_work = Cleaner(name=cleaner)

    for customer in list_of_customers:
        CinemaBar.sell_product(product=customer.food, customer=customer.name)
    cinema_hall.movie_session(movie_name=movie,
                              customers=list_of_customers,
                              cleaning_staff=cleaner_work)
