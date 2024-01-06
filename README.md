# Movie Database Project Documentation

## Overview

The `python_SKILLO_FinalProject` project is a command-line interface (CLI) application designed to manage a database of movies. Its primary goal is to provide users with a simple and interactive way to add, retrieve, and explore information about movies. Whether you're a movie enthusiast or just looking to organize your watchlist, this project aims to streamline the management of movie data.

### Key Features

1. **Add New Movies**: Users can add new movies to the database by providing essential details such as title, description, release year, genre, rating, and their preference (favorite or not).

2. **List All Movies**: Retrieve a comprehensive list of all movies stored in the database, displaying key information for each entry.

3. **Get Movie Details**: Obtain detailed information about a specific movie using its unique identifier.

4. **Search Movies**: Conduct searches based on movie titles, making it easy to find specific films of interest.

5. **Mark as Favorite**: Users have the option to mark a movie as a favorite, enhancing personalization and categorization.

6. **Top Movies by Category**: Explore top movies based on categories such as user likes, newest releases, or a specific genre.

## Table of Contents

- [Files](#files)
- [How to Run the Project](#how-to-run-the-project)
- [Command-Line Interface (CLI)](#command-line-interface-cli)
- [Functions and Modules](#functions-and-modules)
- [Error Handling](#error-handling)
- [Future Improvements](#future-improvements)

## Files

### 1. `main.py`

#### Purpose

The `main.py` file serves as the entry point for the Movie Database project. It is responsible for defining the command-line interface (CLI) using the Click library and orchestrating the execution of various commands to interact with the movie database.

#### Usage

To run the Movie Database project, use the following command:
```bash
python main.py <command> [options]


python main.py movadd --title "Dirty Ace 2" --description "Mind-bending thriller" --release-year 2010 --genre "Sci-Fi" --rating 8.8


python main.py movlst


python main.py movdt 11


python main.py movsrch "Dirty Ace 2"


python main.py movfv 11


python main.py movcat liked
```
### 2. `movie.py`

#### Purpose

The `movie.py` file defines the `Movie` class, which serves as the fundamental data structure for representing movies in the Movie Database project. This class encapsulates essential information about a movie, such as its title, description, release year, genre, rating, and user preference (favorite or not).

#### `Movie` Class

The `Movie` class has the following attributes:

- `id`: Unique identifier for the movie.
- `title`: Title of the movie.
- `description`: Brief description of the movie.
- `release_year`: Release year of the movie.
- `genre`: Genre of the movie.
- `rating`: Rating of the movie.
- `favorite`: User preference for the movie (default is not a favorite).

Additionally, the class provides a `__str__` method, allowing for a human-readable representation of a movie instance.

#### Example Usage

To create a new `Movie` instance and print its details, you can use the following example:

```bash
from Movie import Movie

# Create a movie instance
movie = Movie(id=11, title="Dirty Ace 2", description="Mind-bending thriller", release_year=2010, genre="Sci-Fi", rating=8.8, favorite=False)

# Print movie details
print(movie)
```
### 3. `movie_database.py`

#### Purpose

The `movie_database.py` file contains the `MovieDatabase` class, responsible for managing the SQLite database and providing functions to interact with movie data in the Movie Database project. It handles operations such as adding new movies, retrieving movie details, listing movies, searching for movies, marking movies as favorites, and obtaining top movies by different categories.

#### `MovieDatabase` Class

The `MovieDatabase` class has the following key functionalities:

- **Initialization (`__init__`):** Establishes a connection to the SQLite database and ensures that the required table (`movies`) is created if it doesn't exist.

- **Adding a Movie (`add_movie`):** Inserts a new movie into the database.

- **Listing Movies (`list_movies`):** Retrieves and displays details of all movies stored in the database.

- **Getting Movie by ID (`get_movie_by_id`):** Retrieves details of a specific movie based on its unique identifier.

- **Searching Movies (`search_movies`):** Searches for movies based on their titles.

- **Marking as Favorite (`mark_as_favorite`):** Updates the favorite status of a movie.

- **Getting Top Movies (`get_top_movies`):** Retrieves top movies based on specified categories such as user likes, newest releases, or a specific genre.

#### Example Usage

To use the `MovieDatabase` class in your Movie Database project, you can create an instance and call its methods. Below is an example:

```bash
from movie_database import MovieDatabase
from Movie import Movie

# Create a MovieDatabase instance
movie_db = MovieDatabase("movie_database.db")

# Create a Movie instance
movie = Movie(id=11, title="Dirty Ace 2", description="Mind-bending thriller", release_year=2010, genre="Sci-Fi", rating=8.8, favorite=False)

# Add the movie to the database
movie_db.add_movie(movie)

# List all movies in the database
movie_db.list_movies()

# Get details of a specific movie
movie_details = movie_db.get_movie_by_id(11)
print(movie_details)

# Search for movies
search_results = movie_db.search_movies("Dirty Ace 2")
print(search_results)

# Mark a movie as a favorite
movie_db.mark_as_favorite(1)

# Get top movies by category
top_movies = movie_db.get_top_movies("liked")
print(top_movies)
```
## How to Run the Project

### Prerequisites

1. **Python Installation:**
   Ensure that Python is installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

2. **Dependencies Installation:**
   Install the required dependencies using the following command:
```bash
   pip install -r requirements.txt
   
```
### Running the CLI
1. **Navigate to the Project Directory:**
   Open a terminal or command prompt and navigate to the directory where the project files are located.
2. **Execute the CLI Commands:**
   Run the Movie Database CLI commands using the main.py file. Below are some examples of common commands:
  
#### Add a new movie:
```bash
   python main.py movadd --title "Inception" --description "Mind-bending thriller" --release-year 2010 --genre "Sci-Fi" --rating 8.8
   
```

#### List all movies:
```bash
   python main.py movlst
   
```

#### Get details of a movie:
```bash
   python main.py movdt 11
   
```
#### Search for movies:
```bash
   python main.py movsrch "Dirty Ace 2"
   
```
#### Mark a movie as a favorite:
```bash
   python main.py movfv 11
   
```
#### Get top movies by category:
```bash
   python main.py movcat liked
   
```

## Command-Line Interface (CLI)

The Movie Database project offers a Command-Line Interface (CLI) for users to interact with and manage movie data. Below are the available commands and their respective functionalities:

### 1. `movadd`

**Purpose:**
Add a new movie to the database.

**Usage:**
```bash
python main.py movadd --title "Dirty Ace 2" --description "Mind-bending thriller" --release-year 2010 --genre "Sci-Fi" --rating 8.8
## Functions and Modules
```

**Options:**

--***id:*** ID for the movie (optional).
--***title:*** Title of the movie (required).
--***description:*** Description of the movie (required).
--***release-year:*** Release year of the movie (required).
--***genre:*** Genre of the movie (required).
--***rating:*** Rating of the movie (required).
--***favorite:*** User preference for this movie (optional).

### 2. `movlst`

**Purpose:**
List all movies in the database.

**Usage:**
```bash
python main.py movlst
```
### 3. `movdt`

**Purpose:**
Get details of a specific movie.

**Usage:**
```bash
python main.py movdt 1
```
### 4. `movsrch`

**Purpose:**
Search for movies based on their titles.

**Usage:**
```bash
python main.py movsrch "Dirty Ace 2"
```
### 5. `movfv`

**Purpose:**
Mark a movie as a favorite.

**Usage:**
```bash
python main.py movfv 11
```
### 6. `movcat`

**Purpose:**
Get top movies by category.

**Usage:**
```bash
python main.py movcat liked
```
Describe important functions and modules in your project.

### 7. `Movie` Class**: Explanation of the `Movie` class in `movie.py`.
 The Movie class, defined in the movie.py file, represents a movie object with various attributes such as id, title, description, release_year, genre, rating, and favorite.

#### 7.1 `Attributes:`
  -  ****id****:The unique identifier for the movie.
  -  ****title:**** The title of the movie.
  -   ****release_year:**** The year in which the movie was released.
  -   ****genre:**** The genre or category of the movie.
  -   ****rating:**** The rating assigned to the movie.
  -   ****favorite:**** A flag indicating whether the movie is marked as a favorite.
#### 7.2 `Methods:`

  -  __init__(self, id, title, description, release_year, genre, rating, favorite): The constructor method initializes a Movie object with the provided attributes.
  -  __str__(self): The __str__ method returns a string representation of the movie, displaying its attributes.

- **`MovieDatabase` Class**: Explanation of the `MovieDatabase` class in `movie_database.py`.

### 8. MovieDatabase Class.
 The MovieDatabase class, defined in the movie_database.py file, is responsible for managing the movie database, including database creation, movie addition, listing movies, retrieving movie details, searching for movies, marking movies as favorites, and getting top movies by category.
#### 8.1 `Attributes:`
  -  ****db_file****: The file path of the SQLite database used for storing movie data.
  - ****conn:**** The SQLite database connection.
#### 8.2 `Methods:`
  - ****__init__(self, db_file)****:The constructor method initializes a `MovieDatabase` object, creating the movies table if it doesn't exist.
  - ****_create_table(self)****: A private method to create the movies table in the database.
  - ****add_movie(self, movie)****: Adds a movie to the database.
  - ****list_movies(self)****: Lists all movies in the database.
  - ****get_movie_by_id(self, movie_id)****: Retrieves a movie by its ID.
  - ****search_movies(self, query)****: Searches for movies based on their titles.
  - ****mark_as_favorite(self, movie_id)****: Marks a movie as a favorite.
  - ****get_top_movies(self, category, limit=5)****: Gets the top movies based on the specified category.

## Error Handling

### main.py
#### 1 `Command-Line Interface (CLI) Errors:`
  - The CLI commands utilize the Click library, which automatically handles missing or incorrect command-line arguments and options. Click will display helpful error messages to guide users.
#### 2 `Database Connection Errors:`
  - The project initializes a connection to the SQLite database (`movie_database.db`). Connection errors, such as the absence of the database file, are handled with appropriate error messages.

### movie.py
#### 1 `Movie Initialization Errors:`
   - The `Movie` class constructor (__init__) ensures that mandatory attributes such as `title`, `description`, `release_year`, `genre`, and `rating` are provided. If any of these attributes are missing, an error is raised.
### movie_database.py
#### 1 `Database Connection Errors:`
   - The `MovieDatabase`  class initializes a connection to the SQLite database. Connection errors, such as the absence of the database file or table creation failure, are handled with informative error messages.
#### 2 `Movie Addition Errors:`
   - When adding a movie to the database, the `add_movie` method ensures that the provided movie instance has all the necessary attributes. If any attribute is missing, an error is raised.
#### 3 `Movie Retrieval Errors:`
   - The `get_movie_by_id` method checks for the existence of a movie with the specified ID. If the movie is not found, an error message is displayed.
#### 4 `Search Errors:`
   - The `search_movies` method handles errors related to searching for movies based on titles. If no matching movies are found, it provides a relevant error message.
#### 5 `Favorite Marking Errors:`
   - The `mark_as_favorite` method handles errors related to marking movies as favorites. If the specified movie ID is not found, an error message is displayed.
#### 6 `Top Movies Retrieval Errors:`
   - The `get_top_movies` method ensures that the specified category is valid and handles errors related to retrieving top movies. If no movies are found for the specified category, it provides a relevant error message.

## Future Impruvements
The Movie Database project provides a foundation for managing a movie collection. Here are potential areas for future improvements and enhancements:
### 1 User Authentication and Authorization:
 - Implement user authentication and authorization mechanisms to allow different users to have personalized movie collections and preferences.
### 2 Enhanced Search Functionality:
 - Improve the search functionality to support more advanced queries, such as searching by genre, release year range, or rating range.
### 3 User Ratings and Reviews:
 - Introduce a feature for users to rate movies and leave reviews. Display aggregate ratings and reviews for each movie.
### 4 Data Validation and Sanitization:
 - Implement more robust data validation and sanitization mechanisms to ensure that data stored in the database is accurate and secure.
### 5  Web Interface:
 - Develop a web-based interface for the Movie Database, allowing users to interact with the application through a user-friendly website.
