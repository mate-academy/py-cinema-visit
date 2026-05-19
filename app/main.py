from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: Cleaner,
        movie: str | list) -> None:

    customer_list = [
        Customer(name=customer["name"],
                 food=customer["food"]) for customer in customers]
    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_instance)
