from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(customers: list, cleaner: str, movie: str) -> None:
    result_list = []
    for element in customers:
        result_list.append(Customer(element["name"], element["food"]))
    for customer in result_list:
        CinemaBar.sell_product(customer.food, customer)
    for element in result_list:
        CinemaHall.movie_session(movie, element.name, cleaner)
