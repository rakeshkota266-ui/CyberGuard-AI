import boto3

bedrock = boto3.client(
    "bedrock-runtime",
    region_name="ap-south-1"
)


def ask_cyberguard(question):
    response = bedrock.converse(
        modelId="global.amazon.nova-2-lite-v1:0",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": f"""
You are CyberGuard AI, an IoT cybersecurity assistant.

User question:
{question}

Give a simple, professional cybersecurity answer.
If the situation looks dangerous, clearly mention the risk level.
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


if __name__ == "__main__":
    question = input("Ask CyberGuard AI: ")
    answer = ask_cyberguard(question)

    print("\n===== CYBERGUARD AI =====")
    print(answer)