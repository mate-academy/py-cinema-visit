from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    list_of_customers = [
        Customer(name=customer["name"],
                 food=customer["food"]
                 )
        for customer in customers
    ]
    for person in list_of_customers:
        CinemaBar.sell_product(person, person.food)
    hall_num = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)
    hall_num.movie_session(
        movie_name=movie,
        customers_list=list_of_customers,
        cleaning_staff=staff
    )
