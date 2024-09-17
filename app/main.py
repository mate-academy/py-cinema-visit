from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    for cust in customers:
        customer = Customer(name=cust["name"], food=cust["food"])
        cinema_bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(movie_name=movie,
                       customers=[
                           Customer(name=cust["name"],
                                    food=cust["food"]
                                    ) for cust in customers],
                       cleaning_staff=cleaner_obj)
