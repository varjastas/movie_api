from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    movies = cursor.execute('SELECT * FROM movies').fetchall()
    conn.close()
    
    return jsonify([{"id": movie[0], "title": movie[1], "description": movie[2], "release_year": movie[3]} for movie in movies])

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    movie = cursor.execute('SELECT * FROM movies WHERE id=?', (id,)).fetchone()
    conn.close()

    # Return movie if found
    if movie:
        return jsonify({"id": movie[0], "title": movie[1], "description": movie[2], "release_year": movie[3]})
    else:
        return jsonify({"error": "Not found"}), 404

@app.route('/movies', methods=['POST'])
def create_movie():
    if not request.json or not 'title' in request.json or not 'release_year' in request.json:
        return jsonify({'error': 'Bad request'}), 400

    new_movie = (request.json['title'], request.json.get('description', ""), request.json['release_year'])

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    # Insert new movie into the database
    cursor.execute('INSERT INTO movies(title, description, release_year) VALUES (?, ?, ?)', new_movie)
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": new_id, "title": new_movie[0], "description": new_movie[1], "release_year": new_movie[2]})

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    if not request.json:
        return jsonify({'error': 'Bad request, JSON missing'}), 400

    if 'title' not in request.json or 'release_year' not in request.json:
        return jsonify({'error': 'Bad request, title and release_year are required'}), 400

    title = request.json['title']
    release_year = request.json['release_year']
    description = request.json.get('description')

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Update the movie
    if description is not None:
        cursor.execute('UPDATE movies SET title = ?, description = ?, release_year = ? WHERE id = ?', (title, description, release_year, id))
    else:
        cursor.execute('UPDATE movies SET title = ?, release_year = ? WHERE id = ?', (title, release_year, id))
    
    # Check if the movie was found and updated
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Not found"}), 404

    conn.commit()
    conn.close()

    # Return the updated movie
    return jsonify({"id": id, "title": title, "description": description, "release_year": release_year})


if __name__ == '__main__':
    # The application listens on all public IPs
    app.run(debug=True, host='0.0.0.0')
