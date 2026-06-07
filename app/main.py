from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers_obj = [
        Customer(name=customer.get("name"), food=customer.get("food"))
        for customer in customers
    ]
    cleaner_obj = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    for customer_obj in customers_obj:
        CinemaBar.sell_product(
            customer=customer_obj, product=customer_obj.food
        )
    cinema_hall.movie_session(
        movie_name=movie, customers=customers_obj, cleaning_staff=cleaner_obj
    )
