# zertoautomation_webhook
An agile, lightweight, and asynchronous automation framework that processes Zerto ZVMA recovery webhooks. Built with FastAPI and pyVmomi, it decouples webhook receipt from out-of-band orchestration logic to completely eliminate script runtime timeouts during critical recovery windows.

This framework completely decouples the API webhook receiving layer from deep infrastructure logic (e.g., vCenter manipulations via pyVmomi), preventing ZVMA script runtime timeouts while offering centralized control over Disaster Recovery (DR) or Cyber Resilience validation procedures.
🚀 Key Architectural Advantages
Non-Blocking Execution: Leverages FastAPI's BackgroundTasks to send an immediate acknowledgment (200 OK) back to the ZVMA container, allowing the Zerto VPG workflow to complete instantly.
Fully Decoupled Design: Environment configurations (.env), framework initialization logic (config.py), logging behaviors, and actual DR actions (customlogic_automation_worker.py) live in completely isolated modules.
Production Ready: Built-in rotating file log management with strict file-size constraints to safeguard host disk targets.
Thread-Safe Handshaking: Utilizes modern, native pyVmomi connection contexts to communicate securely with target VMware vCenter Server infrastructure.
📂 Repository Structure
Plaintext
├── .env                         # Local environment settings & vCenter credentials
├── config.py                    # Strong-typed configuration loader (Pydantic-Settings)
├── logger_config.py             # Thread-safe rotating log manager
├── customlogic_automation_worker.py # Centralized playbook execution (pyVmomi / vCenter tasks)
├── main.py                      # FastAPI core engine and webhook endpoints
├── test_main.py                 # Pytest test suite for validating webhook contracts
├── start_server.bat             # Single-click startup file for Windows Server deployments
└── start_server.sh              # Terminal startup execution script for Linux hosts
🛠️ Quick Start
Prerequisites
Ensure Python 3.11+ is installed and appended to your system's PATH.
Configure Environment Context
Create a .env file in the root directory:
Ini, TOML
ENVIRONMENT=production
DEBUG=false
VC_HOST=**.**.**.**
VC_USER=administrator@vsphere.local
VC_PASS=YourSecurePassword Here
Launching the Framework
On Windows:
Double-click start_server.bat. This automatically updates required dependencies (fastapi, uvicorn, pyvmomi, pydantic-settings, etc.) and mounts the service cluster listening on port 8000.
On Linux:
Grant execution permission and start the service script:
Bash
chmod +x start_server.sh
./start_server.sh
🧪 Validating the Webhook Pipeline
You can run automated test assertions to verify contract mechanics by running:
Bash
pytest
To trigger manually via a webhook simulator (or your ZVMA post-recovery script pipeline), target the endpoint with a JSON body map matching your virtual protection groups:
HTTP
POST http://<your_server_ip>:8000/zerto
Content-Type: application/json
{
"vpgName": "Production_Core_VPG"
}
