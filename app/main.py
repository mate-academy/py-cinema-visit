from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    all_customers = [
        Customer(
            name=cust_dict["name"],
            food=cust_dict["food"]
        )
        for cust_dict in customers
    ]

    for cust in all_customers:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie,
                       customers=all_customers,
                       cleaning_staff=cleaning_staff)
