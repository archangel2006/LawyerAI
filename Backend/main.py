import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Import LlamaIndex components correctly
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # Allow all origins

# Function to load the Indian Constitution PDF and create an index
def load_legal_documents():
    try:
        reader = SimpleDirectoryReader(input_files=["./indian_constitution.pdf"])  # Update path if needed
        docs = reader.load_data()

        if not docs:
            print("⚠️ Warning: No documents found in the provided path.")
            return None

        # Create an index for querying the PDF
        index = VectorStoreIndex.from_documents(docs)
        return index.as_query_engine()
    except Exception as e:
        print(f"❌ Error loading legal documents: {str(e)}")
        return None

# Load the document once when the server starts
query_engine = load_legal_documents()

# Chat API Endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400  # Bad Request

    user_message = data["message"]

    if not query_engine:
        return jsonify({"error": "Legal document index is unavailable. Please try again later."}), 500  # Server Error

    chatbot_response = query_engine.query(user_message)
    response_text = chatbot_response.response if chatbot_response else "I couldn't find a direct reference in the Constitution."

    return jsonify({"response": response_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port if available
    app.run(host="0.0.0.0", port=port, debug=True)  # Allow external access
