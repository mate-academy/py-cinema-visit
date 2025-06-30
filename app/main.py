def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    """Simulate cinema visit scenario with food sales, movie watching and cleaning.

    Args:
        customers: List of dicts with 'name' and 'food' keys
        hall_number: Number of cinema hall
        cleaner: Name of cleaner
        movie: Movie title
    """
    # Process food sales
    for customer in customers:
        print(f"Cinema bar sold {customer['food']} to {customer['name']}.")

    # Movie starts
    print(f"\"{movie}\" started in hall number {hall_number}.")

    # Customers watching
    for customer in customers:
        print(f"{customer['name']} is watching \"{movie}\".")

    # Movie ends
    print(f"\"{movie}\" ended.")

    # Cleaning
    print(f"Cleaner {cleaner} is cleaning hall number {hall_number}.")
