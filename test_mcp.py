import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


async def main():
    async with streamable_http_client(
        "http://127.0.0.1:8000/mcp"
    ) as (read_stream, write_stream):

        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()

            print("\n===== MCP TOOLS =====")

            for tool in tools.tools:
                print(f"- {tool.name}")

            result = await session.call_tool(
                "analyze_threat",
                {
                    "device": "Smart Camera",
                    "traffic_multiplier": 5.0
                }
            )

            print("\n===== CYBERGUARD RESULT =====")
            print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())