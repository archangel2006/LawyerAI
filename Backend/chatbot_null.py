import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key securely
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API key is missing. Please set GEMINI_API_KEY in the .env file.")

genai.configure(api_key=API_KEY)

# Initialize the chatbot model
model = genai.GenerativeModel("gemini-1.0")
chat = model.start_chat()

# Function to get chatbot response
def get_chatbot_response(user_input):
    response = chat.send_message(user_input)
    return response.text

# if you want to use the chatbot in standalone mode
# if __name__ == "__main__":
#     print("Welcome to LawyerAI Chatbot! Type 'exit' or 'quit' to stop.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             break
#         print("LawyerAI:", get_chatbot_response(user_input))
