from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document

# Load documents
loader = DirectoryLoader('data/', glob="*.json")
documents = loader.load()


embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
vectorstore = Chroma.from_documents(documents, embedding=embeddings)
retriever = vectorstore.as_retriever()
retrieved_docs = retriever.get_relevant_documents(query)

# Create language model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Create RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=vectorstore.as_retriever()
)

# Query function
def query_documents(question):
    return rag_chain.run(question)

# Example usage
print(query_documents("Your specific question here"))
