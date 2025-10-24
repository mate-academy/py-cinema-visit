from typing import List, Dict, Final


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name: Final[str] = name
        self.food: Final[str] = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name: Final[str] = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(
        self,
        movie_name: str,
        customers: List[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number)


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objs: List[Customer] = [
        Customer(name=customer_dict["name"], food=customer_dict["food"])
        for customer_dict in customers
    ]

    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
