from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    list_customers = [Customer(name=customer.get("name"),
                               food=customer.get("food"))
                      for customer in customers]
    staff = Cleaner(cleaner)
    for customer in list_customers:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie,
                       customers=list_customers,
                       cleaning_staff=staff)
