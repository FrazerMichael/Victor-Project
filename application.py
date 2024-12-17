from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def get_version():
    try:
        with open("version.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"  # Default version if file not found

@app.route('/')
def index():
    version = get_version()  # Get the current version
    return render_template("index.html", version=version)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    return jsonify({"message": f"Hello {name}!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

