# 🧠 MCP-MultiTool AI Agent

A powerful multi-agent AI system built using [LangChain](https://www.langchain.com/), [MCP (Model Control Protocol)](https://github.com/langchain-ai/mcp), and [Streamlit](https://streamlit.io/). This app connects multiple external tools (Math, Weather, and Web Search) to a single AI agent for real-time interaction and factual reasoning.

---

## 🔧 Features

- 🧮 **Math Tool** – Solves basic math problems like addition and multiplication.
- 🌤️ **Weather Tool** – Retrieves real-time weather using the OpenWeather API.
- 🔍 **Search Tool** – Uses DuckDuckGo and Wikipedia to answer recent/factual queries.
- 💬 **Conversational UI** – User-friendly Streamlit interface to ask and view questions.
- 🧩 **MCP Integration** – Modular architecture for defining tools via FastMCP.

---

## 🚀 How It Works

- Each tool (math, weather, search) runs as an independent MCP server.
- A central agent (`client.py`) connects to the tools using LangChain's `MultiModalClient`.
- The `Streamlit` frontend (`app.py`) allows users to interact with the agent in real-time.
- Questions are routed to the appropriate tool based on the intent.

---

## 🗂️ Folder Structure

MCPSERVERLangchain/
├── app.py # Streamlit frontend
├── client.py # LangChain agent setup
├── mathserver.py # Math MCP server
├── weather.py # Weather MCP server
├── search_tool.py # DuckDuckGo + Wikipedia tool
├── .gitignore
└── README.md


---

## 🔑 Requirements

- Python 3.10+
- Streamlit
- LangChain
- FastMCP
- OpenWeather API key (set in `.env`)

Install dependencies:

```bash
pip install -r requirements.txt

🛠️ Run the App
streamlit run app.py

📦 .env File Example
ini
Copy
Edit
OPENWEATHER_API_KEY=your_openweather_key
GROQ_API_KEY=groq api key

📄 License
MIT License

✨ Author
Awais Aslam


📌 Inspired by
LangChain AI Agents

MCP Protocol

Real-World Multi-Agent Systems
