import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001"
)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/home/rfourcade/dev/mcp-course/mcp-crash-course/servers/math_server.py"],
)


async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
