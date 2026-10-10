from mcp.server.mcpserver import MCPServer

server = MCPServer("CyberGuard AI")


@server.tool()
async def analyze_threat(
    device: str,
    traffic_multiplier: float
) -> str:
    """Analyze a suspicious IoT device traffic spike."""

    if traffic_multiplier >= 5:
        risk = "HIGH"
        message = (
            f"Device '{device}' is generating "
            f"{traffic_multiplier}x its normal traffic. "
            "This may indicate malware, data exfiltration, "
            "or botnet activity."
        )

    elif traffic_multiplier >= 2:
        risk = "MEDIUM"
        message = (
            f"Device '{device}' is generating "
            f"{traffic_multiplier}x its normal traffic. "
            "Further investigation is recommended."
        )

    else:
        risk = "LOW"
        message = (
            f"Device '{device}' traffic is "
            f"{traffic_multiplier}x normal. "
            "No major anomaly detected."
        )

    return f"Risk Level: {risk}\n{message}"


if __name__ == "__main__":
    server.run(
    transport="streamable-http",
    port=8001
)