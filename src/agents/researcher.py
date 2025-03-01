from crewai import Agent
from src.retriever.vectorstore import VectorStore
from src.logger import logging

class ResearcherAgent:
    def __init__(self):
        self.vector_store = VectorStore()
        self.agent = Agent(
            role="Researcher",
            goal="Find the most relevant research materials for a given query.",
            backstory="An AI-powered researcher with expertise in finding relevant academic and industry materials.",
            verbose=True
        )

    def fetch_documents(self, query):
        """Fetch relevant documents using FAISS."""
        logging.info(f"ResearcherAgent: Searching for query '{query}'")
        return self.vector_store.search(query, k=5)
