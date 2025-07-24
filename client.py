from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            "args": ["mathserver.py"],
            "transport": "stdio",
        },
        "weather": {
            "command": "python",  # Ensure server is running here
            "args": ["weather.py"],
            "transport": "stdio",
    }
    }
)


    # Load Groq API Key
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    
    os.environ["GROQ_API_KEY"] = groq_api_key

    # Load tools and model
    tools = await client.get_tools()
    model = ChatGroq(model="llama3-70b-8192")
    agent = create_react_agent(model, tools)

    print("\n🔗 AI Agent is ready! Type a question or 'exit' to quit.\n")

    while True:
        user_input = input("🧠 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        response = await agent.ainvoke({"messages": [{"role": "user", "content": user_input}]})
        print("🤖 Agent:", response['messages'][-1].content)
        print()

asyncio.run(main())
