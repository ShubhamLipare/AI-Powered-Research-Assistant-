from crewai import Agent
from langchain_core.prompts import PromptTemplate
from src.logger import logging

class SummarizerAgent:
    def __init__(self):
        self.agent = Agent(
            role="Summarizer",
            goal="Summarize the retrieved research documents into concise, clear points.",
            backstory="An AI expert in summarization, skilled at distilling complex information.",
            verbose=True
        )

    def summarize(self, documents):
        """Summarizes the given documents."""
        logging.info("SummarizerAgent: Summarizing documents...")
        combined_text = "\n".join([doc.page_content for doc in documents])
        
        prompt = PromptTemplate(
            template="Summarize the following research material:\n{content}",
            input_variables=["content"]
        )
        
        return prompt.format(content=combined_text)
