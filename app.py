from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_books():
    # URL of the first service
    server_url = os.environ.get('SERVER_URL')

    # Make a request to the first service
    response = requests.get(server_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract books data from the response
        books = response.json()["books"]

        # Get the genre parameter from the query string
        genre = request.args.get('genre')

        # Filter books based on the specified genre
        if genre:
            filtered_books = [book for book in books if genre.lower() in book['genre'].lower()]
            return jsonify({"books": filtered_books})
        else:
            return jsonify({"books": books[2]})
    else:
        return jsonify({"error": "Failed to retrieve books from the first service"}), 500

if __name__ == '__main__':
    app.run(debug=True)