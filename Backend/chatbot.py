from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

# Function to load the PDF and create an index
def load_legal_documents():
    reader = SimpleDirectoryReader(input_files=["./indian_constitution.pdf"])  # Update path if needed
    docs = reader.load_data()
    
    # Create an index for querying the PDF
    index = GPTVectorStoreIndex.from_documents(docs)
    
    return index.as_query_engine()

# Initialize the chatbot engine
query_engine = load_legal_documents()

# Function to get chatbot response
def get_chatbot_response(user_input):
    response = query_engine.query(user_input)
    return response.response if response else "I couldn't find a direct reference in the Constitution."
