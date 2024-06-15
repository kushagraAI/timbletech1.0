# TMDB MOVIE App

This Django application fetches data from the TMDB API, saves it to a database, and provides RESTful API endpoints for interacting with movies, reviews, and comments. It includes user authentication using JWT, permissions for different user roles, and features such as movie recommendations, ratings, search, filtering, and pagination. The project is built with Django REST Framework (DRF) and includes Swagger/OpenAPI documentation.

## Table of Contents

- [Installation](git clone https://github.com/kushagraAI/timbletech1.0.git)
- [Running the Project](python manage.py runserver)
- [Running the Tests](python manage.py test)
- [API Endpoints](http://localhost:8000/api/movies)
- [API Endpoints](http://localhost:8000/api/reviews)
- [API Endpoints](http://localhost:8000/api/comments)

### Features

- Fetch and Save Movies: Fetch movie data from TMDB API and save it to the database.
- User Authentication: JWT-based authentication with custom user model.
- CRUD Operations: Create, read, update, and delete operations for movies, reviews, and comments.
- Recommendations: Collaborative filtering-based movie recommendations for users.
- Ratings and Reviews: Users can rate and review movies.
- Comments: Users can comment on reviews.
- Search and Filtering: Search and filter movies, reviews, and comments.
- Pagination: Paginate movie and review lists.
- Swagger/OpenAPI Documentation: API documentation using drf-yasg.
- Postman Collection: Includes a Postman collection with example requests.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (recommended)
- Django (install latest version of Django)
- Django REST Framework (install latest version of Django REST Framework)

### Clone the Repository

```
git clone https://github.com/kushagraAI/timbletech1.0.git
```

## Installation

Follow these steps to set up the project on your local machine:

- Activate virtual environment (if not already activated) and install all required dependencies by running `pip install -r requirements.txt` in a terminal window.

##### Activate virtual Environment =

- "venv\Scripts\activate" (for windows users)
- "source venv/bin/activate" (for linux and macOS users)

### Run the Project

- python manage.py runserver

###Set Up the Database

### Run the following commands to set up the database:

- python manage.py makemigrations
- python manage.py migrate

### Create a Superuser

#### Create a superuser account to access the Django admin panel.

- python manage.py createsuperuser

### Running the Tests

To run the tests, use the following command:

- python manage.py test

### API Endpoints

Here are the main API endpoints provided by the application:

- GET /api/movies/: List all movies
- GET /api/movies/<int:id>/: Retrieve a movie
- POST /api/reviews/: Create a review (authenticated)
- GET /api/reviews/: List all reviews
- POST /api/comments/: Create a comment (authenticated)
- GET /api/comments/: List all comments
- GET /api/recommendations/: Get movie recommendations (authenticated)
- POST /api/token/: Obtain JWT token
- POST /api/token/refresh/: Refresh JWT token

### Authentication

- Login: /api-token-auth/ (POST)
  TMDB API
- List all movies: /api/movies/ (GET) - NO authentication requires
- Create a new destination: /api/movies/ (POST) - Requires authentication
- Retrieve a specific destination: /api/movies/<id>/ (GET)
- Update a specific destination: /api/movies/<id>/ (PUT) - Requires authentication
- Delete a specific destination: /api/movies/<id>/ (DELETE) - Requires authentication

### Postman collections

Soon Be Update here...
