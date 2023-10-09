import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import openai

# Load environment variables from .env file
load_dotenv()

# Get the API key and fine-tuned model ID from the environment
api_key = os.getenv("API_KEY")
fine_tuned_model_id = None

# Check if the API key is set
if not api_key:
    raise ValueError("API_KEY is not set in the .env file")

# Check if the model ID exists in the model.txt file
model_file_path = "model.txt"
if os.path.exists(model_file_path):
    with open(model_file_path, "r") as model_file:
        fine_tuned_model_id = model_file.read().strip()

# Check if the fine-tuned model ID is set
if not fine_tuned_model_id:
    raise ValueError("Fine-tuned model ID is not set in the model.txt file")

# Set the API key
openai.api_key = api_key

# Create a Flask app
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_with_model():
    try:
        # Get user input from the request
        user_message = request.json['message']

        # Create a session with your fine-tuned model
        session = openai.ChatCompletion.create(
            model=fine_tuned_model_id,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # Get the model's response
        response = session['choices'][0]['message']['content']

        # Return the response as JSON
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)