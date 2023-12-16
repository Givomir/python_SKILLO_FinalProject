# movie_database.py
import sqlite3
from Movie import Movie

class MovieDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Create a movies table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                genre TEXT NOT NULL,
                rating REAL NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    def add_movie(self, movie):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Insert the movie into the movies table
        cursor.execute('''
            INSERT INTO movies (title, release_year, genre, rating)
            VALUES (?, ?, ?, ?)
        ''', (movie.title, movie.release_year, movie.genre, movie.rating))

        conn.commit()
        conn.close()

        print("Movie added successfully.")

    def list_movies(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Fetch all movies from the movies table
        cursor.execute('''
            SELECT title, release_year, genre, rating FROM movies
        ''')

        movies = cursor.fetchall()

        conn.close()

        for movie in movies:
            print(f"{movie[0]} ({movie[1]}) - Genre: {movie[2]}, Rating: {movie[3]}")
