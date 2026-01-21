class Customer:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def watch_movie(self, movie_name):
        print(f"{self.name} is watching \"{movie_name}\".")
