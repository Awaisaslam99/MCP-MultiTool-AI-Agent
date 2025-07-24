import streamlit as st
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set Streamlit page config
st.set_page_config(page_title="Multi-AI Agent", page_icon="🤖", layout="centered")
st.title("🤖 Multi-AI Assistant")
st.markdown("Ask **math** questions or get the **weather** for any city!")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []  # each item = {"question": "...", "answer": "..."}

# Initialize session state for agent
if "agent" not in st.session_state:
    async def init_agent():
        client = MultiServerMCPClient({
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "command": "python",
                "args": ["weather.py"],
                "transport": "stdio",
            },
            "search": {
                "command": "python",
                "args": ["search_tool.py"],
                "transport": "stdio",
            }
        })


        tools = await client.get_tools()
        model = ChatGroq(model="llama3-70b-8192")
        return create_react_agent(model, tools)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    st.session_state.agent = loop.run_until_complete(init_agent())

# User input box at the bottom
user_input = st.chat_input("Ask me anything about math or weather...")

# If user submits a question
if user_input:
    async def get_response(user_input):
        agent = st.session_state.agent
        response = await agent.ainvoke({"messages": [{"role": "user", "content": user_input}]})
        return response['messages'][-1].content

    # Run async and store result
    with st.spinner("🤔 Thinking..."):
        response = asyncio.run(get_response(user_input))
        st.session_state.messages.append({
            "question": user_input,
            "answer": response
        })

# Display all previous Q&A
for chat in st.session_state.messages:
    with st.chat_message("user"):
        st.markdown(chat["question"])
    with st.chat_message("assistant"):
        st.markdown(chat["answer"])
