from strands import Agent
from strands.models.ollama import OllamaModel

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2:3b"
)

agent = Agent(
    model=ollama_model,
    tools=[],
    system_prompt="You are a helpful assistant. Be brief."
)

print("\n🤖 Agent: ", end="")

response = agent(
    "Tell me a fun fact about Python programming"
)

print(response)

print("\n✅ Challenge 1 complete!")