from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import asyncio
import boto3

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


app = FastAPI(
    title="CyberGuard AI",
    description="AI-powered IoT Cybersecurity Assistant",
    version="1.0.0"
)


bedrock = boto3.client(
    "bedrock-runtime",
    region_name="ap-south-1"
)


async def get_mcp_analysis(device, traffic):

    async with streamable_http_client(
        "http://127.0.0.1:8001/mcp"
    ) as (read_stream, write_stream):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            await session.initialize()

            result = await session.call_tool(
                "analyze_threat",
                {
                    "device": device,
                    "traffic_multiplier": traffic
                }
            )

            return result.content[0].text


def get_nova_analysis(device, traffic):

    response = bedrock.converse(
        modelId="global.amazon.nova-2-lite-v1:0",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": f"""
You are CyberGuard AI, an IoT cybersecurity assistant.

Device: {device}
Traffic multiplier: {traffic}x normal

Analyze this IoT security situation.

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


@app.get("/")
def home():

    return FileResponse(
        "frontend/index.html"
    )


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "project": "CyberGuard AI"
    }


@app.get("/api/analyze")
async def analyze(
    device: str = Query(...),
    traffic: float = Query(...)
):

    mcp_result = await get_mcp_analysis(
        device,
        traffic
    )

    nova_result = get_nova_analysis(
        device,
        traffic
    )

    if traffic >= 5:
        risk = "HIGH"
    elif traffic >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "risk": risk,
        "mcp_analysis": mcp_result,
        "analysis": nova_result
    }