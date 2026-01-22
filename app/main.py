from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customer_list = []

    for i in range(len(customers)):
        customer_list.append(Customer(customers[i]["name"],
                                      customers[i]["food"]))

    for cust in customer_list:
        CinemaBar.sell_product(customer=cust, product=cust.food)
    hall.movie_session(movie, customer_list, cleaning_staff)


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(
        customers=customers,
        hall_number=hall_number,
        cleaner=cleaner_name,
        movie=movie
    )
