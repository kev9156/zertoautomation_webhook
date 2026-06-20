# zertoautomation_webhook
An agile, lightweight, and asynchronous automation framework that processes Zerto ZVMA recovery webhooks. Built with FastAPI and pyVmomi, it decouples webhook receipt from out-of-band orchestration logic to completely eliminate script runtime timeouts during critical recovery windows.


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

