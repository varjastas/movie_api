import sqlite3

# Connect to the database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# List of movies to insert as fixtures
movies = [
    ("The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", 1994),
    ("The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", 1972),
    ("Pulp Fiction", "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.", 1994),
    ("The Dark Knight", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.", 2008),
    ("Schindler's List", "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.", 1993)
]

# Insert movies into the database
for movie in movies:
    cursor.execute('INSERT INTO movies (title, description, release_year) VALUES (?, ?, ?)', movie)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database populated with 5 movie fixtures.")
