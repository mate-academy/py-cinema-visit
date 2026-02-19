from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int, cleaner: str, movie: str) -> None:
    customer_list: list[Customer] = []

    for customer in customers:
        customer_list.append(Customer(name=customer["name"],
                                      food=customer["food"]))

    for customer_obj in customer_list:
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie,
                       customers=customer_list,
                       cleaning_staff=cleaning_staff)
