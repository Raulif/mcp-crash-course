import asyncio

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")


async def main():
    print("running langchain_client.py")
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/home/rfourcade/dev/mcp-course/mcp-crash-course/servers/math_server.py"
                ],
                "transport": "stdio",
            },
            "weather": {"url": "http://127.0.0.1:8000/sse", "transport": "sse"},
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    result = await agent.ainvoke(
        {
            "messages": "What is 3 * 33 * 333. and then figure out what is the weather like in SF. Once you know that, take the result of the question about the weather, and multiply the result of the math problem by a number equal to the letters of the result of the weather question. give me this final result."
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
