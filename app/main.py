def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str) -> None:
    from app.people.customer import Customer
    from app.people.cinema_staff import Cleaner
    from app.cinema.bar import CinemaBar
    from app.cinema.hall import CinemaHall

    customer_objects = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"], food=customer_data["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_objects.append(customer)

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)
