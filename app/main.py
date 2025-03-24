from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    customer = [Customer(name=customer_data["name"],
                         food=customer_data["food"])
                for customer_data in customers]

    for customer_data in customer:
        CinemaBar.sell_product(product=customer_data.food,
                               customer=customer_data)

    hall.movie_session(movie, customer, cleaner_staff)
