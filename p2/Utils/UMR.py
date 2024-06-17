class UMR:
    def __init__(self, users: list, movies: list, ratings: list):
        self.users = users
        self.movies = movies
        self.ratings = ratings

    def get_users(self) -> list:
        return self.users

    def get_movies(self) -> list:
        return self.movies

    def get_ratings(self) -> list:
        return self.ratings

    def set_users(self, users: list):
        self.users = users

    def set_movies(self, movies: list):
        self.movies = movies

    def set_ratings(self, ratings: list):
        self.ratings = ratings