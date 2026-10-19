from typing import List, Dict, Any


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        print(f"Cinema bar sold {customer.get(\"food\")} to {customer.get(\"name\")}.")

    print(f"\"{movie}\" started in hall number {hall_number}.")

    for customer in customers:
        print(f"{customer.get(\"name\")} is watching \"{movie}\".")

    print(f"\"{movie}\" ended.")
    print(f"Cleaner {cleaner} is cleaning hall number {hall_number}.")
