from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:

    dir_customer = []

    for custom in customers:
        cur_customer = Customer(
            name=custom["name"],
            food=custom["food"]
        )
        dir_customer.append(cur_customer)

        CinemaBar.sell_product(
            product=cur_customer.food,
            customer=cur_customer
        )

    hall = CinemaHall(number=hall_number)
    cleaner_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=dir_customer,
        cleaning_staff=cleaner_staff
    )
