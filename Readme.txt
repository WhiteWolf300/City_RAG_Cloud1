The project provides a summary of Manchester City's 2024-25 Premier League season performance using a RAG (Retrieval Augmented Generation) approach. It uses Google Cloud's Vertex AI and a Streamlit front-end deployed on Cloud Run to get data from a text file and generate a summary based on a given query.

1) Features:

Document Loading: Loads data from a text file (City_CurrentSeason2.txt).

Text Splitting: Splits the document into smaller chunks for efficient processing.

Embeddings: Uses Vertex AI's gemini-embedding-001 model to create vector representations of the text chunks.

Vector Store: Stores and retrieves relevant document chunks using ChromaDB.

Retrieval-Augmented Generation: Utilizes a Vertex AI gemini-2.0-flash model and a defined prompt template to generate a summary based on the retrieved context.

Summary: Provides a summary focusing on key aspects like final position, key players, injuries, and their impact or as per the user prompt.

Web Application: Features an interactive Streamlit UI for user queries and summary display.

Cloud Deployment: The entire application is containerized and deployed on Google Cloud Run for scalability.

2) Requirements
2.1) Required Python Packages:
streamlit
langchain
langchain-community
langchain-core
langchain-text-splitters
chromadb
langchain_google_vertexai

2.2) Google Cloud Setup:
A Google Cloud project with the Vertex AI API and Cloud Run API enabled.

Authentication set up via gcloud auth application-default login.

3) Working
The application is deployed on Google Cloud Run. The user interacts with the Streamlit web interface to input a query. The RAG pipeline then performs the following steps:


Load and Split Content: The City_CurrentSeason2.txt file is loaded and split into overlapping chunks.

Embed: Vector embeddings are created using Vertex AI's gemini-embedding-001 model.

Vector Store: These embeddings are indexed into a ChromaDB vector store.


Semantic Search: The user's query is used to find the most relevant document chunks from the vector store.

LLM Summary: The retrieved context is fed into Vertex AI's gemini-2.0-flash model with a prompt template to generate a concise summary.

4) Deployment
The application is deployed as a containerized service on Google Cloud Run. The deployment process involves:

Building a container image using a Dockerfile.

Pushing the image to Google's Artifact Registry.

Deploying the image to a new Cloud Run service.