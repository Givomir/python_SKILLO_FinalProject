# main.py
import click
from Movie import Movie
from movie_database import MovieDatabase

@click.group()
def cli():
    pass

@cli.command()
@click.option("--id", required=False, help="ID for the movie")
@click.option("--title", required=True, help="Title of the movie")
@click.option("--description", required=True, help="Description of the movie")
@click.option("--release-year", required=True, help="Release year of the movie")
@click.option("--genre", required=True, help="Genre of the movie")
@click.option("--rating", required=True, help="Rating of the movie")
@click.option("--favorite", required=False, help="User preference for this movie")
def movadd(id, title, description, release_year, genre, rating, favorite):
    """Add a new movie."""
    movie = Movie(id, title, description, release_year, genre, rating, favorite)
    movie_db.add_movie(movie)
    click.echo("Movie added successfully.")

@cli.command()
def movlst():
    """List all movies."""
    movie_db.list_movies()

@click.command()
@click.argument('movie_id', required=True)
def movdt(movie_id):
    """Get details of a movie."""
    movie_details = movie_db.get_movie_by_id(movie_id)
    if movie_details:
        click.echo(f"Movie Details: {movie_details}")
    else:
        click.echo(f"Movie with ID {movie_id} not found.")

@click.command()
@click.argument('query', required=True)
def movsrch(query):
    """Search for movies based on their titles."""
    search_results = movie_db.search_movies(query)
    if search_results:
        click.echo("Search Results:")
        for result in search_results:
            click.echo(result)
    else:
        click.echo(f"No movies found with title containing '{query}'.")


@click.command()
@click.argument("movie_id")
def movfv(movie_id):
    """Mark a movie as a favorite."""
    movie_db.mark_as_favorite(movie_id)
    click.echo(f"Movie with ID {movie_id} marked as a favorite.")


# Add the  command to the CLI
cli.add_command(movadd)
cli.add_command(movlst)
cli.add_command(movdt)
cli.add_command(movsrch)
cli.add_command(movfv)

if __name__ == "__main__":
    movie_db = MovieDatabase("movie_database.db")
    cli()
