from crewai import Task
from src.agents.critic import CriticAgent
from src.logger import logging

class CriticTask:
    def __init__(self, summary):
        self.summary = summary
        self.agent = CriticAgent()
        self.task = Task(
            description="Critique and refine the given research summary.",
            agent=self.agent.agent
        )


    def execute(self):
        """Executes the critique task."""
        logging.info("Executing Critic Task...")
        return self.agent.critique(self.summary)
