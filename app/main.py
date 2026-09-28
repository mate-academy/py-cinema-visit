from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    list_customer = []
    for customer in customers:
        current_customer = Customer(
            name=customer["name"],
            food=customer["food"]
        )

        CinemaBar.sell_product(current_customer.food, current_customer)
        list_customer.append(current_customer)

    hall = CinemaHall(number=hall_number)
    cleaner_staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=list_customer,
        cleaning_staff=cleaner_staff
    )


if __name__ == "__main__":
    # Ten kod wykona się tylko przy bezpośrednim uruchomieniu pliku main.py
    sample_customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    cinema_visit(
        customers=sample_customers,
        hall_number=5,
        cleaner="Anna",
        movie="Madagascar"
    )
