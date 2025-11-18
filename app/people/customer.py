class Customer:
    """
    Minimal Customer used by tests.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.tickets: list = []

    def buy_ticket(self, ticket: str) -> None:
        self.tickets.append(ticket)
