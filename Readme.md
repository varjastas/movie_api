# Movie API

A simple Flask REST API to manage movies.

## How to Run

1. Install Flask: `pip install Flask`
2. Run `python database.py` to create the database.
3. Run `python app.py`.
4. You can populate your db with pregenerated movie objects by running populate_db.py
4. Visit http://127.0.0.1:5000/movies in your browser or use a tool like curl or Postman to test the API.


## Docker Instructions

1. Build the Docker image: `docker build -t movie-api .`
2. Run the Docker container: `docker run --name my-movie-api-container -p 8000:5000 movie-api`.
3. Visit http://127.0.0.1:8000/movies in your browser or use a tool like curl or Postman to test the API.
