from solapi import SolapiMessageService
from solapi.model.message import Message
from stock_api import check_price_change
from dotenv import load_dotenv
import os

load_dotenv()

SOLAPI_API_KEY = os.getenv("SOLAPI_API_KEY")
SOLAPI_API_SECRET = os.getenv("SOLAPI_API_SECRET")

solapi_auth = SolapiMessageService(api_key=SOLAPI_API_KEY, api_secret=SOLAPI_API_SECRET)

def up_down_emojis(price_change: float) -> str:
    return "UP" if price_change > 0 else "DOWN"

def send_sms(name, price_change, title_1, title_2, brief_1, brief_2):
    message = Message(
        to="01063971643",
        from_="01063971643",
        text=f"{name}: {price_change}% {up_down_emojis(price_change)}\nHeadLine: {title_1}\nBrief: {brief_1}\n\nHeadLine: {title_2}\nBrief: {brief_2}"
    )
    try:
        response = solapi_auth.send(message)
        print("Sent successfully!")
        return response
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return None




