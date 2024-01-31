from flask import Flask, render_template, jsonify, request
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        # Get the user's input from the form
        author = request.form.get('author')
        title = request.form.get('title')
        genre = request.form.get('genre')

        # URL of the server 
        server_url = os.environ.get('SERVER_URL', "http://books-api.c4c5a9dkepczcvd7.uksouth.azurecontainer.io:5000/" 
)

        # Make a request to the server with the provided filters
        response = requests.get(server_url, params={'author': author, 'title': title, 'genre': genre})
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract books data from the response
            books = response.json()["books"]
            return books
        else:
            return jsonify({"error": "Failed to retrieve books from the server"}), 500
    else:
        # Render the initial HTML page with the search form
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)