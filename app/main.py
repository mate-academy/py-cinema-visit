from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_customers = [Customer(name=customers[i]["name"],
                               food=customers[i]["food"])
                      for i in range(len(customers))]
    for people in list_customers:
        CinemaBar.sell_product(people.food, people)
    clean = Cleaner(cleaner)
    number_hall = CinemaHall(hall_number)
    number_hall.movie_session(movie_name=movie,
                              customers=list_customers,
                              cleaning_staff=clean)
