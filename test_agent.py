import os
import logging
from dotenv import load_dotenv
from resources.registry.agents.file_access_agent import FileAccessAgent
from resources.object_oriented_agents.utils.logger import get_logger

# Set up logging
logger = get_logger("TestScript", level=logging.DEBUG)

# Load environment variables from .env file
load_dotenv()

# Make sure you have set your OpenAI API key in environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set your OPENAI_API_KEY environment variable in .env file")
logger.debug(f"API key loaded successfully: {api_key[:8]}...")

# Create an instance of the FileAccessAgent
agent = FileAccessAgent()

# Test the agent with the traffic_accidents.csv file
user_message = "Can you show me the first few lines of traffic_accidents.csv?"
logger.debug(f"Sending message to agent: {user_message}")
response = agent.task(user_message)
print("\nAgent Response:")
print(response) 