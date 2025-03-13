from llama_index.core import SimpleDirectoryReader, GPTVectorStoreIndex

# Function to load the Indian Constitution PDF and create an index
def load_legal_documents():
    reader = SimpleDirectoryReader(input_files=["./indian_constitution.pdf"])  
    docs = reader.load_data()

    # Create an index for querying the PDF
    index = GPTVectorStoreIndex.from_documents(docs)
    return index.as_query_engine()

# Load the document once when the module is imported
query_engine = load_legal_documents()

def get_legal_response(user_message):
    chatbot_response = query_engine.query(user_message)
    return chatbot_response.response if chatbot_response else "I couldn't find a direct reference in the Constitution."
