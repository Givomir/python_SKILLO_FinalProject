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
    try:
        # Create a movie instance with the provided arguments
        movie = Movie(id, title, description, release_year, genre, rating, favorite)
        # Add the movie to the database
        movie_db.add_movie(movie)
        click.echo()
    except click.ClickException as e:
        raise click.ClickException(f"Error adding the movie: {e}")
@cli.command()
def movlst():
     """List all movies."""
        #list all movies in the database
     try:
         # List all movies in the database
         movie_db.list_movies()
     except click.ClickException as e:
         raise click.ClickException(f"Error listing movies: {e}")

@click.command()
@click.argument('movie_id', required=True)
def movdt(movie_id):
    """Get details of a movie."""
    try:
        movie_details = movie_db.get_movie_by_id(movie_id)
        if movie_details:
            click.echo(f"Movie Details: {movie_details}")
        else:
            raise click.ClickException(f"Movie with ID {movie_id} not found.")
    except click.ClickException as e:
        raise click.ClickException(f"Error getting movie details: {e}")

@click.command()
@click.argument('query', required=True)
def movsrch(query):
    """Search for movies based on their titles."""
    try:
        search_results = movie_db.search_movies(query)
        if search_results:
            click.echo("Search Results:")
            for result in search_results:
                click.echo(result)
        else:
            raise click.ClickException(f"No movies found with title containing '{query}'.")
    except click.ClickException as e:
        raise click.ClickException(f"Error searching for movies: {e}")


@click.command()
@click.argument("movie_id")
def movfv(movie_id):
    """Mark a movie as a favorite."""
    try:
        movie_db.mark_as_favorite(movie_id)
        click.echo(f"Movie with ID {movie_id} marked as a favorite.")
    except click.ClickException as e:
        raise click.ClickException(f"Error marking movie as a favorite: {e}")

@click.command()
@click.argument('category', type=click.Choice(['liked', 'newest', 'genre']))
def movcat(category):
    """Get top movies by category."""
    try:
        top_movies = movie_db.get_top_movies(category)
        if top_movies:
            click.echo(f"Top Movies in {category.capitalize()}:\n")
            for movie in top_movies:
                click.echo(movie)
        else:
            raise click.ClickException(f"No movies found for the specified category.")
    except click.ClickException as e:
        raise click.ClickException(f"Error getting top movies: {e}")

# Add the  command to the CLI
cli.add_command(movadd)
cli.add_command(movlst)
cli.add_command(movdt)
cli.add_command(movsrch)
cli.add_command(movfv)
cli.add_command(movcat)

if __name__ == "__main__":
    movie_db = MovieDatabase("movie_database.db")
    cli()
