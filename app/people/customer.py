class Customer:

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> str:
        message = f'{self.name} is watching "{movie}".'
        print(message)
        return message
