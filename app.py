from flask import Flask, jsonify, request
import anthropic


# Initialize the Flask app
app = Flask(__name__)

client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="",)

def call_claude(user_inp, is_slang):

    if is_slang == True:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system="You are well aware of Gen-Z slang and will convert requested sentences into proper American English. Do nothing further.",
            messages=[
                {"role": "user", "content": f"Convert the following Gen-Z slang into proper English - {user_inp}"}
            ]
        )   
        print(type(message.content))
        print(message.content[0].text)
        return message.content[0].text
    else:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system="You will convert the requested sentence to Gen-Z slang. Do nothing further.",
            messages=[
                {"role": "user", "content": f"Convert the following sentence into Gen-Z slang - {user_inp}"}
            ]
        )
        print(type(message.content))
        print(message.content[0].text)
        return message.content[0].text

# Define a simple route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Define a sample GET endpoint
@app.route('/api/greet', methods=['GET'])
def greet():
    # Get the 'name' parameter from the query string, defaulting to 'World'
    name = request.args.get('name', 'World')
    is_genz_slang = False
    user_input = request.args.get('user_input', 'World')
    slang_input = request.args.get('slang_input', 'n')
    if slang_input == "y":
        is_genz_slang = True
    oput = call_claude(user_inp=user_input, is_slang=is_genz_slang)
    return jsonify({"message": f"{oput}"})

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
