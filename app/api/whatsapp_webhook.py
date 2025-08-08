from fastapi import APIRouter


router = APIRouter()

@router.get("/webhook")
async def whatsapp_webhook():
    return {"message": "WhatsApp Webhook Endpoint"}
  