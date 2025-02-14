from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    number: int,
    cleaner: str,
    movie: str
) -> None:
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(number=number)
    hall.movie_session(
        movie_name=movie,
        customers=[
            Customer(name=c["name"], food=c["food"]) for c in customers],
        cleaning_staff=Cleaner(name=cleaner)
    )
