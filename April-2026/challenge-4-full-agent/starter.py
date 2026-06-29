import os
from datetime import datetime

from strands import Agent, tool
from strands_tools import calculator

# ---------------------------------
# Environment Configuration
# ---------------------------------

os.environ["BYPASS_TOOL_CONSENT"] = "true"

# ---------------------------------
# Model Configuration
# ---------------------------------

MODEL = "us.amazon.nova-pro-v1:0"

# ---------------------------------
# Custom Tools
# ---------------------------------

@tool
def weather(city: str) -> str:
    """Return weather information for a city."""
    return f"The weather in {city} is sunny, 32°C."


@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from a birth date (YYYY-MM-DD)."""

    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()

    age = today.year - birth.year

    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1

    return f"Age: {age} years"


# ---------------------------------
# Create Agent
# ---------------------------------

agent = Agent(
    model=MODEL,
    tools=[
        calculator,
        weather,
        age_calculator
    ],
    system_prompt="You are a helpful assistant."
)

# ---------------------------------
# Chat Loop
# ---------------------------------

print("\n🤖 Full Agent Ready!")
print("Type 'quit' to exit.")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "quit":
        break

    print("\nAgent:")
    print(agent(user_input))

print("\n✅ Challenge 4 complete!")