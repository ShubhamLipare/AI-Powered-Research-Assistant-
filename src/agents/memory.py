from langchain.memory import ConversationBufferMemory

class AgentMemory:
    def __init__(self):
        """Initialize conversation memory for storing user queries and responses."""
        self.memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
    
    def add_interaction(self,user_query,agent_response):
        """Store user query and agent response in memory."""
        self.memory.save_context({"input":user_query},{"output":agent_response})

    def retrieve_memory(self):
        """Retrieve stored conversation history."""
        return self.memory.load_memory_variables({}).get(["chat_history"],[])
    
    def clear_memory(self):
        self.memory.clear()
