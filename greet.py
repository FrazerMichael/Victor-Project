from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    return jsonify({"message": f"Hello {name}!"})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port, debug=False)  # Disable debug mode for production

