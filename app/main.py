from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    clients_list = []

    for customer in customers:
        client = Customer(name=customer.get("name"), food=customer.get("food"))
        clients_list.append(client)
        CinemaBar.sell_product(product=client.food, customer=client)

    hall.movie_session(movie_name=movie,
                       customers=clients_list,
                       cleaning_staff=cleaner)
