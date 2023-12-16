# main.py
import argparse
from Movie import Movie
from movie_database import MovieDatabase

if __name__ == "__main__":
    movie_db = MovieDatabase("movie_database.db")

    parser = argparse.ArgumentParser(description="Movie Database CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add the 'add-movie' command
    add_movie_parser = subparsers.add_parser("movadd", help="Add a new movie")
    add_movie_parser.add_argument("--title", required=True, help="Title of the movie")
    add_movie_parser.add_argument("--release-year", required=True, help="Release year of the movie")
    add_movie_parser.add_argument("--genre", required=True, help="Genre of the movie")
    add_movie_parser.add_argument("--rating", required=True, help="Rating of the movie")

    # Add the 'list-movies' command
    subparsers.add_parser("movlst", help="List all movies")

    args = parser.parse_args()

    if args.command == "movadd":
        movie = Movie(args.title, args.release_year, args.genre, args.rating)
        movie_db.add_movie(movie)
    elif args.command == "movlst":
        movie_db.list_movies()
    else:
        print("Invalid command. Use 'movadd' or 'movlst'.")