import openai
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("API_KEY")

# Check if the API key is set
if not api_key:
    raise ValueError("API_KEY is not set in the .env file")

# Set the API key
openai.api_key = api_key

# Fine-tuned model ID obtained from your fine-tuning job
fine_tuned_model_id = "your_fine_tuned_model_id_here"

# Create a session with your fine-tuned model
session = openai.ChatCompletion.create(
    model=fine_tuned_model_id,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
)

# Start a conversation by asking about a specific topic
user_message = "Háblame sobre Decis Evo®"
session = openai.ChatCompletion.create(
    model=fine_tuned_model_id,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]
)

response = session['choices'][0]['message']['content']
print("Respuesta del modelo:", response)

# Continue the conversation by asking more questions
user_message = "¿Cuáles son los ingredientes activos de Decis Expert®?"
session = openai.ChatCompletion.create(
    model=fine_tuned_model_id,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]
)

response = session['choices'][0]['message']['content']
print("Respuesta del modelo:", response)

# Continue with additional questions as needed