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
    cleaning_staff = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    customers_list = [
        Customer(name=customer.get("name"), food=customer.get("food"))
        for customer in customers
    ]
    for customer in customers_list:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie_name=movie, customers=customers_list,
                              cleaning_staff=cleaning_staff)
