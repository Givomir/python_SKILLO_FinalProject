# movie.py
class Movie:
    def __init__(self, id, title, description, release_year, genre, rating, favorite):
        self.id = id
        self.title = title
        self.description = description
        self.release_year = release_year
        self.genre = genre
        self.rating = rating
        self.favorite = favorite

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.release_year} - {self.genre} - {self.rating} - {self.favorite}"

