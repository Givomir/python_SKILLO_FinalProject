# movie_database.py
import sqlite3
from Movie import Movie

class MovieDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self._create_table()
        self.conn = sqlite3.connect(db_file)


    def _create_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Create a movies table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                genre TEXT NOT NULL,
                rating REAL NOT NULL,
                favorite INTEGER NOT NULL DEFAULT 0
            )
        ''')

        conn.commit()
        conn.close()

    def add_movie(self, movie):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Insert the movie into the movies table
        cursor.execute('''
            INSERT INTO movies (id, title, description, release_year, genre, rating, favorite)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (movie.id, movie.title, movie.description, movie.release_year, movie.genre, movie.rating, movie.favorite))

        conn.commit()
        conn.close()

        print("Movie added successfully.")

    def list_movies(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Fetch all movies from the movies table
        cursor.execute('''
            SELECT id, title, description, release_year, genre, rating, favorite FROM movies
        ''')

        movies = cursor.fetchall()

        conn.close()

        for movie in movies:
            print(f"ID:{movie[0]} Title:{movie[1]} -Description: {movie[2]}, Release Year: {movie[3]}, - Genre: {movie[4]}, Rating: {movie[5]}, Favorite: {movie[6]}")


    def get_movie_by_id(self, movie_id):
        """Get a movie by its ID."""
        query = "SELECT * FROM movies WHERE ID = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (movie_id,))
        movie_data = cursor.fetchone()

        if movie_data:
            # Return a dictionary with movie details
            return {
                'ID': movie_data[0],
                'title': movie_data[1],
                'description': movie_data[2],
                'release_year': movie_data[3],
                'genre': movie_data[4],
                'rating': movie_data[5],
                'favorite': movie_data[6]
                # Add more fields as needed
            }
        else:
            # Movie with the specified ID not found
            self.conn.commit()
            self.conn.close()
            return None
        # Implement the logic to retrieve a movie by its ID from the database
        # Return the Movie object if found, otherwise return None


    def search_movies(self, query):
        """Search for movies based on their titles."""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Fetch movies from the movies table that match the search query
        cursor.execute('''
            SELECT id, title, description, release_year, genre, rating FROM movies
            WHERE title LIKE ?
        ''', (f'%{query}%',))

        movies = cursor.fetchall()

        conn.close()

        search_results = []
        for movie in movies:
            search_results.append(f"-ID {movie[0]} -Title ({movie[1]}) -Description({movie[2]}) -release_year: {movie[3]} -Genre: {movie[4]} -Rating: {movie[5]}")

        return search_results


    def mark_as_favorite(self, movie_id):
        """Mark a movie as a favorite."""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Update the favorite status of the movie
        cursor.execute('''
           UPDATE movies SET favorite = favorite + 1 WHERE ID = ?
        ''', (movie_id,))

        conn.commit()
        conn.close()

    def get_top_movies(self, category, limit=5):
        """Get the top movies based on the specified category."""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        if category == 'liked':
            cursor.execute('''
                SELECT ID, title, Description, release_year, genre, rating, favorite 
                FROM movies
                ORDER BY favorite DESC
                LIMIT ?
            ''', (limit,))
        elif category == 'newest':
            cursor.execute('''
                SELECT ID, title, Description, release_year, genre, rating, favorite
                FROM movies
                ORDER BY release_year DESC
                LIMIT ?
            ''', (limit,))
        elif category == 'genre':
            genre = input("Enter the genre: ")  # You can modify this to accept user input
            cursor.execute('''
                SELECT ID, title, Description, release_year, genre, rating, favorite 
                FROM movies
                WHERE genre = ?
                ORDER BY rating DESC
                LIMIT ?
            ''', (genre, limit))
        else:
            conn.close()
            return None

        movies = cursor.fetchall()
        conn.close()

        top_movies = []
        for movie in movies:
            top_movies.append(
                f"-ID {movie[0]} -Title ({movie[1]}) -Description({movie[2]}) -release_year: {movie[3]} -Genre: {movie[4]} -Rating: {movie[5]} -Favorite: {movie[6]}"
            )

        return top_movies