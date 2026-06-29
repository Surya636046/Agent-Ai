from strands import Agent
from strands.tools.mcp import MCPClient

from mcp import (
    StdioServerParameters,
    stdio_client
)

# ---------------------------------
# Model Configuration
# ---------------------------------

MODEL = "us.amazon.nova-pro-v1:0"

# ---------------------------------
# MCP Server Configuration
# ---------------------------------

aws_docs_mcp = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="awslabs.aws-documentation-mcp-server"
        )
    )
)

# ---------------------------------
# Start MCP Client
# ---------------------------------

with aws_docs_mcp:

    # Load all tools from the MCP server
    tools = aws_docs_mcp.list_tools_sync()

    # Create the Agent
    agent = Agent(
        model=MODEL,
        tools=tools,
        system_prompt="""
You are an AWS Learning Assistant.
Explain AWS concepts simply.
"""
    )

    print("\n☁ AWS Learning Assistant")
    print("Type 'quit' to exit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        print("\nAssistant:\n")
        print(agent(user_input))
        print()