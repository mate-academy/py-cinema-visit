from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_obg = [Customer(cus["name"], cus["food"]) for cus in customers]
    cleaner_obg = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for cus in customer_obg:
        CinemaBar.sell_product(product=cus.food, customer=cus)

    hall.movie_session(movie_name=movie,
                       customers=customer_obg,
                       cleaning_stuff=cleaner_obg)
