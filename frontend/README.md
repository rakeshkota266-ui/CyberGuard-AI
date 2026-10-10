# 🛡️ CyberGuard AI

**AI-Powered IoT Cybersecurity Threat Detection and Analysis**

CyberGuard AI is a prototype cybersecurity assistant that analyzes IoT device traffic indicators, classifies potential risk levels, and generates AI-powered security analysis and recommendations.

## 🚀 Project Overview

IoT devices such as smart cameras and sensors can be exposed to unusual network activity. CyberGuard AI provides a dashboard for submitting device information, reviewing risk classifications, and viewing AI-generated security guidance.

## ✨ Features

- **AI-powered analysis:** Uses Amazon Bedrock with Amazon Nova 2 Lite.
- **MCP integration:** Connects the application to an MCP server that exposes the `analyze_threat` tool.
- **Risk classification:** Displays High, Medium, or Low risk based on the configured traffic multiplier rules.
- **Security recommendations:** Presents guidance appropriate to the reported risk level.
- **Dashboard counters:** Tracks the number of analyses in each risk category.
- **Recent activity history:** Stores the latest 10 successful analyses in browser local storage.
- **Responsive interface:** Provides a dark-themed dashboard for desktop and mobile screens.

## 🧰 Technology Stack

- Python
- FastAPI
- Model Context Protocol (MCP)
- Amazon Bedrock
- Amazon Nova 2 Lite
- HTML, CSS, and JavaScript
- AWS CLI

## 🏗️ Architecture

1. The user enters an IoT device name and traffic multiplier in the web dashboard.
2. The dashboard sends a request to the FastAPI backend.
3. The backend communicates with the MCP server and invokes the configured threat-analysis tool.
4. The backend requests AI analysis from Amazon Bedrock.
5. The dashboard displays the risk classification, analysis, and recommendations.
6. The browser stores risk counters and recent activity locally.

## 📁 Project Structure

```text
CyberGuard-AI/
├── backend/
│   ├── main.py
│   └── mcp_server.py
├── frontend/
│   └── index.html
├── README.md
└── .gitignore
```

Other project files may be present depending on the development setup.

## ⚙️ Prerequisites

- Python installed
- AWS CLI configured and authenticated
- Access to Amazon Bedrock and the selected Nova 2 Lite model in the configured AWS region
- Required Python packages installed in your virtual environment

## ▶️ Run Locally

Open a terminal in the project root and activate your virtual environment.

**Terminal 1 — Start the MCP server**

```bash
python backend/mcp_server.py
```

**Terminal 2 — Start the FastAPI backend**

```bash
python -m uvicorn backend.main:app --reload --port 8000
```

Open the dashboard:

http://127.0.0.1:8000

Check the backend health endpoint:

http://127.0.0.1:8000/health

Run these commands from the project root with your virtual environment activated. On Windows, use the equivalent Python commands supported by your terminal.

## 🔐 Security and Configuration

- Authenticate to AWS using an appropriate AWS CLI or IAM Identity Center session.
- Do not commit AWS credentials, access keys, `.env` files containing secrets, or other sensitive information.
- Restrict permissions to the minimum required for the application.
- Do not expose development servers publicly without suitable authentication and security controls.

## ⚠️ Limitations

CyberGuard AI is a prototype. Its risk classification uses a configured traffic multiplier and should not be interpreted as proof that a device has been compromised. AI-generated recommendations are advisory and depend on the input and model response.

The current dashboard stores its counters and activity history in the browser rather than a central database. It does not yet provide persistent server-side audit logs or independently validated intrusion detection.

## 🔮 Future Enhancements

- Integrate real IoT network telemetry.
- Add dataset-based anomaly detection and model evaluation.
- Provide authenticated users and role-based access.
- Store security events in a database.
- Add alerting, visual analytics, and deployment automation.
- Evaluate detection precision, recall, and false-positive rates.

## 👨‍💻 Project

**CyberGuard AI — AI-powered IoT cybersecurity assistant**

Developed as a prototype for an AI and cybersecurity hackathon.
