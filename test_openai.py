import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No API key found")

# Create client
client = OpenAI(api_key=api_key)

# Test a simple completion
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say hello!"}]
)

print(response.choices[0].message.content) 