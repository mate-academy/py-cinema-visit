from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def main() -> None:
    customers = [
        Customer(name="Bob", food="Coca-cola"),
        Customer(name="Alex", food="popcorn")
    ]

    for customer in customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number=5)

    cleaning_staff = Cleaner(name="Anna")

    hall.movie_session(
        movie_name="Madagascar",
        customers=customers,
        cleaning_staff=cleaning_staff
    )


if __name__ == "__main__":
    main()
