from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()  # Parse JSON from the request
    name = data.get('name')  # Extract the 'name' field
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    return jsonify({"message": f"Hello {name}!"})

if __name__ == '__main__':
    app.run(debug=True)
