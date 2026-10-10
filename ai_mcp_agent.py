import asyncio
import boto3

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


bedrock = boto3.client(
    "bedrock-runtime",
    region_name="ap-south-1"
)


async def analyze_with_mcp(device, traffic_multiplier):

    async with streamable_http_client(
        "http://127.0.0.1:8000/mcp"
    ) as (read_stream, write_stream):

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            result = await session.call_tool(
                "analyze_threat",
                {
                    "device": device,
                    "traffic_multiplier": traffic_multiplier
                }
            )

            return result.content[0].text


def ask_nova(question):

    response = bedrock.converse(
        modelId="global.amazon.nova-2-lite-v1:0",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": f"""
You are CyberGuard AI, an IoT cybersecurity assistant.

User situation:
{question}

Provide:
1. Risk assessment
2. Possible causes
3. Recommended actions

Keep the answer simple and professional.
"""
                    }
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 500,
            "temperature": 0.3
        }
    )

    return response["output"]["message"]["content"][0]["text"]


async def main():

    device = "Smart Camera"
    traffic_multiplier = 5.0

    print("\n===== MCP THREAT ANALYSIS =====")

    mcp_result = await analyze_with_mcp(
        device,
        traffic_multiplier
    )

    print(mcp_result)

    print("\n===== NOVA 2 LITE ANALYSIS =====")

    question = (
        f"The device '{device}' is generating "
        f"{traffic_multiplier}x its normal network traffic."
    )

    ai_result = ask_nova(question)

    print(ai_result)


if __name__ == "__main__":
    asyncio.run(main())