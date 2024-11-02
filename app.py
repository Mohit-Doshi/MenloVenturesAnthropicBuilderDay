from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Define a sample GET endpoint
@app.route('/api/greet', methods=['GET'])
def greet():
    # Get the 'name' parameter from the query string, defaulting to 'World'
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

# Define a sample POST endpoint
@app.route('/api/data', methods=['POST'])
def receive_data():
    # Get JSON data from the request
    data = request.json
    # Process data (example: echo it back in response)
    return jsonify({"received_data": data})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
