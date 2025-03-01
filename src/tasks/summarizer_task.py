from src.logger import logging
from src.agents.summarizer import SummarizerAgent
from crewai import Task

class SummarizeTask:
    def __init__(self,document):
        self.agent=SummarizerAgent()
        self.document=document
        self.task = Task(
            description="Summarize the given research documents into key points.",
            agent=self.agent.agent
        )

    def execute(self):
        """Executes the summarization task."""
        logging.info("Executing Summarization Task...")
        return self.agent.summarize(self.document)