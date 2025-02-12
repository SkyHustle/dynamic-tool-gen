from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create client
client = OpenAI()

# Test a simple completion
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say hello!"}]
)

print(response.choices[0].message.content) 