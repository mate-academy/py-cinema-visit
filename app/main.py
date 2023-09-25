from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie: str,
) -> None:
    list_of_classed_customers = []
    for cust in customers:
        person = Customer(name=cust["name"], food=cust["food"])
        cb = CinemaBar()
        cb.sell_product(customer=person, product=person.food)
        list_of_classed_customers.append(person)

    number_of_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaning_staff)
    number_of_hall.movie_session(
        movie_name=movie,
        customers=list_of_classed_customers,
        cleaning_stuff=cleaner)
