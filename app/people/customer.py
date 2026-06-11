class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching \"{movie}\".')

# It was more convenient to refer to an instance of class
# than to a name by using instance.name
# before brining me down because of extra method
# wright description of task more understandable
