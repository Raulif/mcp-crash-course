import asyncio
import os

from dotenv import load_dotenv
from httpx import Client
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/home/rfourcade/dev/mcp-course/mcp-crash-course/servers/math_server.py"],
)


async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialize")
            tools = await load_mcp_tools(session)

            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke(
                {"messages": [HumanMessage(content="What is 3 * 50 + 10?")]}
            )
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
