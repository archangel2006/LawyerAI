from flask import Flask, request, jsonify
from flask_cors import CORS

# Import LlamaIndex components correctly
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # Allow all origins

# Function to load the Indian Constitution PDF and create an index
def load_legal_documents():
    reader = SimpleDirectoryReader(input_files=["./indian_constitution.pdf"])  # Update path if needed
    docs = reader.load_data()

    # Create an index for querying the PDF
    index = VectorStoreIndex.from_documents(docs)
    return index.as_query_engine()

# Load the document once when the server starts
query_engine = load_legal_documents()

# Chat API Endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400  # Bad Request

    user_message = data["message"]
    chatbot_response = query_engine.query(user_message)
    response_text = chatbot_response.response if chatbot_response else "I couldn't find a direct reference in the Constitution."

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Allow external access
