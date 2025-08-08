from fastapi import FastAPI 
from app.api.whatsapp_webhook import router as whatsapp_webhook_router  
from app.api.test import router as whatsapp_webhook_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
  
app.include_router(whatsapp_webhook_router, prefix="/api", tags=["whatsapp-webhook"])