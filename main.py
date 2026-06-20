from fastapi import FastAPI, BackgroundTasks
from config import settings
from logger_config import logger
from customlogic_automation_worker import centralized_automation

#This acts as your API engine gateway, taking the request and shifting it straight to the background worker.

app = FastAPI(title="Zerto Enterprise Automation Framework")

@app.post("/zerto")
async def trigger_from_zvma(payload: dict, background_tasks: BackgroundTasks):
    vpg_name = payload.get("vpgName", "Unknown_VPG")
    logger.info(f"Webhook event registered for target VPG: {vpg_name}")
    
    # Hand off execution to the decoupled module instantly
    background_tasks.add_task(centralized_automation, vpg_name)
    
    return {"status": "accepted", "target_vpg": vpg_name}