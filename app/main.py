from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    for visitor in range(len(customers)):
        customers[visitor] = Customer(name=customers[visitor]["name"],
                                      food=customers[visitor]["food"])
        CinemaBar.sell_product(product=customers[visitor].food,
                               customer=customers[visitor])

    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customers, cleaning_staff=cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"},
    {"name": "Alina", "food": "peaches"}
]

hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number,
             cleaner=cleaner_name, movie=movie)
