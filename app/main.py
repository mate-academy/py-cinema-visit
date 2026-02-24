from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie, customers, hall_number, cleaner):
    customer_instances = []

    for c_data in customers:
        new_customer = Customer(name=c_data["name"], food=c_data["food"])
        customer_instances.append(new_customer)
        CinemaBar.sell_product(product=new_customer.food, customer=new_customer)

    hall = CinemaHall(hall_number=hall_number)
    staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=staff)


if __name__ == "__main__":
    customers_list = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]

    cinema_visit(
        movie="Madagascar",
        customers=customers_list,
        hall_number=5,
        cleaner="Anna"
    )