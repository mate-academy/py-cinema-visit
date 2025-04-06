from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(

        customers: list[dict],
        hall_number: int,
        cleaner: str, movie: str

) -> None:

    customers_list = [Customer(cus["name"], cus["food"]) for cus in customers]

    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)

    cleaning_person = Cleaner(cleaner)

    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaning_person
    )
