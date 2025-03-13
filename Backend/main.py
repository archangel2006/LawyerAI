from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_chatbot_response  # Updated function name

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # Allow all origins

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400  # Bad Request
    
    user_message = data["message"]
    chatbot_response = get_chatbot_response(user_message)
    
    return jsonify({"response": chatbot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Allow external access
