import os
from datetime import datetime

from strands import Agent, tool
from strands_tools import calculator

# Bypass tool consent prompt
os.environ["BYPASS_TOOL_CONSENT"] = "true"

# Amazon Bedrock Model
MODEL = "us.amazon.nova-pro-v1:0"


# ---------------------------
# Custom Tools
# ---------------------------

@tool
def weather(city: str) -> str:
    """Get weather for a city."""
    return f"The weather in {city} is sunny, 32°C."


@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from YYYY-MM-DD."""
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()

    age = today.year - birth.year

    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1

    return f"Age: {age} years"


# ---------------------------
# Create Agent
# ---------------------------

agent = Agent(
    model=MODEL,
    tools=[calculator, weather, age_calculator],
    system_prompt="You are a helpful assistant."
)

# ---------------------------
# Test Calculator
# ---------------------------

print("\n🧮 Math Test")
print(agent("What is 42 * 17?"))

# ---------------------------
# Test Weather Tool
# ---------------------------

print("\n🌤 Weather Test")
print(agent("What's the weather in Chennai?"))

# ---------------------------
# Test Age Calculator
# ---------------------------

print("\n🎂 Age Test")
print(agent("How old is someone born on 2000-05-15?"))

# ---------------------------
# Completion Message
# ---------------------------

print("\n✅ Challenge 2 complete!")
