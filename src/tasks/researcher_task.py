from crewai import Task
from src.agents.researcher import ResearcherAgent
from src.logger import logging

class ResearcherTask:
    def __init__(self,query):
        self.query=query
        self.agent=ResearcherAgent()
        self.task=Task(
            description=f"Find relevant research materials for: {query}",
            agent=self.agent
        )

    def execute(self):
        """Executes the research task."""
        logging.info(f"Executing Research Task for query: {self.query}")
        return self.agent.fetch_documents(self.query)
        