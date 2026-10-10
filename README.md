# CyberGuard AI — Intelligent IoT Threat Detection

CyberGuard AI is an AI-assisted cybersecurity project designed to analyze IoT device traffic indicators and generate readable threat assessments using AWS Bedrock and the Model Context Protocol (MCP).

## Project Overview

IoT devices such as smart cameras and sensors can be exposed to unusual network activity. CyberGuard AI demonstrates how traffic indicators can be analyzed and presented through a simple web dashboard to help users understand potential risks.

## Features

- Interactive web dashboard for IoT threat analysis
- FastAPI backend for handling analysis requests
- MCP server exposing a threat-analysis tool
- AWS Bedrock integration for AI-generated explanations
- Traffic multiplier input for testing different scenarios
- Risk summary and readable analysis report

## Technology Stack

- Python
- FastAPI
- AWS Bedrock — Amazon Nova 2 Lite
- Model Context Protocol (MCP)
- HTML, CSS and JavaScript
- Uvicorn

## Architecture

1. The user selects an IoT device and enters a traffic multiplier in the dashboard.
2. The frontend sends the request to the FastAPI backend.
3. The backend calls the MCP server to perform the threat-analysis step.
4. The backend uses AWS Bedrock to generate an explanatory report.
5. The dashboard displays the result.

## Project Structure

```text
CyberGuard-AI/
├── backend/
│   ├── main.py
│   └── mcp_server.py
├── frontend/
│   └── index.html
├── ai_agent.py
├── ai_mcp_agent.py
├── test_mcp.py
├── README.md
└── .gitignore
```

## Prerequisites

- Python installed
- AWS CLI installed and authenticated
- Access to AWS Bedrock and the selected model in your AWS region
- Git installed

## Run Locally

Open two PowerShell terminals in the project directory and activate your virtual environment in each:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies if needed:

```powershell
pip install fastapi uvicorn boto3 python-dotenv pandas scikit-learn "mcp[cli]" "botocore[crt]" requests
```

### Terminal 1 — Start the MCP server

```powershell
python backend\mcp_server.py
```

### Terminal 2 — Start the web backend

```powershell
python -m uvicorn backend.main:app --reload --port 8000
```

Open the dashboard:

http://127.0.0.1:8000

Health check:

http://127.0.0.1:8000/health

## AWS Configuration

Configure AWS authentication using the AWS CLI or another supported credential provider. Ensure the selected AWS identity has permission to invoke the configured Bedrock model.

Do not commit AWS credentials, access keys, tokens, or `.env` files to GitHub.

## Important Limitations

- This is a demonstration project, not a production-grade intrusion detection system.
- A risk level derived from a traffic multiplier is a demonstration indicator; it does not prove that a device has been compromised.
- AI-generated explanations may be inaccurate and should not be treated as definitive security findings.
- Real-world deployment would require validated datasets, robust detection models, logging, monitoring, and security testing.

## Future Improvements

- Integrate validated IoT network traffic datasets.
- Add a trained and evaluated threat-detection model.
- Improve explainability and false-positive analysis.
- Add historical reports and monitoring.
- Deploy the application with appropriate authentication and security controls.

## Author

Developed as an AI-assisted IoT cybersecurity demonstration project for learning and hackathon development.
