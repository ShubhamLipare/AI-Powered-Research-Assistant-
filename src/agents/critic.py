from crewai import Agent
from langchain_core.prompts import PromptTemplate
from src.logger import logging

class CriticAgent:
    def __init__(self):
        self.agent = Agent(
            role="Critic",
            goal="Review and refine summaries to ensure clarity and correctness.",
            backstory="A meticulous AI critic ensuring high-quality research summaries.",
            verbose=True
        )

    def critique(self, summary):
        """Reviews and refines the summary for clarity."""
        logging.info("CriticAgent: Reviewing the summary...")
        
        prompt = PromptTemplate(
            template="Critique and refine the following summary:\n{summary}",
            input_variables=["summary"]
        )
        
        return prompt.format(summary=summary)
