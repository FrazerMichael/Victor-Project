from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Serve the static HTML file (index.html) from the static folder
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    return jsonify({"message": f"Hello {name}!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

